(function(angular, undefined){

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

            $scope.portfolio = new Portfolio();
            $scope.user = new User();
            window.s = $scope;

            var player;
            $scope.playerReady = false;
            youtubePlayerApi.loadPlayer().then(function(p){
                player = p;
                $scope.playerReady = true;
            });

            $scope.$watch('portfolio.video.youtube_id', function(vid, oldvid) {
                if (!vid || vid === oldvid) return;
                if (player) player.cueVideoById(vid);
                VideoData.load(vid).then(function(data){
                    $scope.portfolio.video.name = data.entry.title.$t;
                });
            });

            function showFieldErrors(response) {
                $scope.errors = response.data;
                var messages = [];
                for (var att in response.data) {
                    var message = response.data[att];
                    if(Portfolio.fields && Portfolio.fields[att]) {
                        message = Portfolio.fields[att].label + ': ' + message;
                    }
                    messages.push(message);
                }
                $scope.alert.error('Encontramos alguns erros!', messages, true);
            }

            $scope.saveThumb = function() {
                if ($scope.thumbfile && $scope.portfolio.id) {
                    if ($scope.thumbfile.size > 120000) {
                        $scope.alert.warn('Por favor, escolha uma imagem menor.');
                        return;
                    }
                    var fu = new FormUpload();
                    fu.addField('thumbnail', $scope.thumbfile);
                    // return a new promise that file will be uploaded
                    return fu.sendTo('/api/portfoliothumbs/' + $scope.portfolio.id)
                    .then(function(){
                        $scope.alert.success('A imagem foi atualizada.');
                    });
                }
            };

            $scope.savePortfolio = function() {
                if(!$scope.portfolio.hasVideo()){
                    delete $scope.portfolio.video;
                }
                $scope.portfolio.description = 'Por favor, insira aqui uma descrição detalhada do portfolio';
                $scope.portfolio.saveOrUpdate()
                .then(function(){
                    return $scope.saveThumb();
                })
                .then(function(){
                    $scope.alert.success('Alterações salvas com sucesso!');
                })['catch'](showFieldErrors);
            };

            $scope.publishPortfolio = function() {
                $scope.portfolio.status = 'published';
                $scope.savePortfolio();
            };

            $scope.deletePortfolio = function() {
                if(!confirm('Tem certeza que deseja remover este item do seu portfolio?')) return;

                $scope.portfolio.$delete()
                .then(function(){
                    document.location.href = '/';
                });
            };


            if (window.portfolioId !== undefined) {
                $scope.portfolio.$get({id: portfolioId})

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
            }
        }]);
})(window.angular);
