(function(angular){

    var app = angular.module('homepage.controllers', []);

    app.controller('CoursesCarouselCtrl', ['$scope', function($scope) {
        console.log('oi');
        $scope.myInterval = 1000;
    }]);
})(window.angular);
