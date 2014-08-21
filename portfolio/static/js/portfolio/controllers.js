(function(angular){

    var app = angular.module('portfolio.controllers', []);

    app.controller('PortfolioEditController',
        ['$scope', 'Portfolio', 'User', '$filter', 'youtubePlayerApi', 'VideoData', 'FormUpload',
        function($scope, Portfolio, User, $filter, youtubePlayerApi, VideoData, FormUpload) {

            $scope.errors = {};
            var httpErrors = {
                '400': 'os campos não foram preenchidos corretamente.',
                '403': 'você não tem permissão para ver o conteúdo nesta página.',
                '404': 'este curso não existe!'
            };

            $scope.portfolio = new portfolio();
            $scope.user = new user();
            window.s = $scope;

            var player;
            $scope.playerready = false;
            youtubeplayerapi.loadplayer().then(function(p){
                player = p;
                $scope.playerready = true;
            });

            $scope.$watch('portfolio.video.youtube_id', function(vid, oldvid) {
                if (!vid || vid === oldvid) return;
                if (player) player.cuevideobyid(vid);
                videodata.load(vid).then(function(data){
                    $scope.portfolio.video.name = data.entry.title.$t;
                });
            });

            function showfielderrors(response) {
                $scope.errors = response.data;
                var messages = [];
                for(var att in response.data) {
                    var message = response.data[att];
                    if(portfolio.fields && portfolio.fields[att]) {
                        message = portfolio.fields[att].label + ': ' + message;
                    }
                    messages.push(message);
                }
                $scope.alert.error('encontramos alguns erros!', messages, true);
            }

            $scope.savethumb = function() {
                if ($scope.thumbfile && $scope.portfolio.id) {
                    var fu = new formupload();
                    fu.addfield('thumbnail', $scope.thumbfile);
                    // return a new promise that file will be uploaded
                    return fu.sendto('/api/portfoliothumbs/' + $scope.portfolio.id)
                    .then(function(){
                        $scope.alert.success('A imagem foi atualizada.');
                    });
                }
            };

            $scope.saveportfolio = function() {
                if(!$scope.portfolio.hasvideo()){
                    delete $scope.portfolio.video;
                }
                $scope.portfolio.description='Por favor, insira aqui uma descrição detalhada do portfolio';
                $scope.portfolio.saveorupdate()
                .then(function(){
                    return $scope.savethumb();
                })
                .then(function(){
                    $scope.alert.success('alterações salvas com sucesso!');
                })['catch'](showfielderrors);
            };

            $scope.publishportfolio = function() {
                $scope.portfolio.status = 'published';
                $scope.saveportfolio();
            };

            $scope.deleteportfolio = function() {
                if(!confirm('Tem certeza que deseja remover este item do seu portfolio?')) return;

                $scope.portfolio.$delete()
                .then(function(){
                    document.location.href = '/';
                });
            };

            var match = document.location.href.match(/portfolio\/([\w.+-]+)\/(new|\d+)/);

            if( match ) {
                console.log(window.userId);
                if('new' === match[2]){
                    $scope.portfolio.user = window.userId;
                }

                else{
                    $scope.portfolio.$get({id: match[2]})

                    .then(function(portfolio){
                        if(portfolio.video) {
                            youtubePlayerApi.videoId = portfolio.video.youtube_id;
                        }
                        document.title = 'Portfolio: {0}'.format(portfolio.name);
                        $scope.portfolios=Portfolio.query({status: 'published',user:portfolio.user});
                        $scope.addThumb = !portfolio.thumbnail_url;
                        // course_material and forum urls
                        $scope.user.$get({id: portfolio.user});
                        return $scope.user.promise;

                    })['catch'](function(resp){
                        $scope.alert.error(httpErrors[resp.status.toString()]);
                    })['finally'](function(){
                        $scope.statusList = Portfolio.fields.status.choices;
                    });
                }}
        }]);
})(window.angular);
