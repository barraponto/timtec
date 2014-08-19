(function(angular){

    var app = angular.module('homepage.controllers', []);

    app.controller('CoursesCarouselCtrl', ['$scope', function($scope) {
        $scope.myInterval = 8000;
    }]);
})(window.angular);
