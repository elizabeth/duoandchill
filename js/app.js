// Debug Stuff
var DEBUG_MODE = true;
var debugVars = {};

var debugMsg = function(msg) {
    if (DEBUG_MODE)
      console.log('!!! DEBUG !!! ' + msg);
};

//  Create Angular App
var ngApp = angular.module('ngApp', ['ngRoute']);

// Stores route information
ngApp.config(function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'views/home.html',
            controller: 'CtrlHome'
        })
        .when('/friend/', {
            templateUrl: 'views/friend.html',
            controller: 'CtrlFriend'
        })
        .when('/register/', {
            templateUrl: 'views/register.html',
            controller: 'CtrlRegister'
        })
        .when('/login/', {
            templateUrl: 'views/login.html',
            controller: 'CtrlLogin'
        })
});

// Header (Nav Bar)
ngApp.controller('CtrlNav', ['$scope', '$location', function($scope, $location) {
    $scope.isActive = function (viewLocation) {
        var active = (viewLocation === $location.path());
        return active;
    };
}]);

ngApp.controller('CtrlHome', ['$scope', '$location', function($scope, $location) {

}]);

ngApp.controller('CtrlFriend', ['$scope', '$location', function($scope, $location) {

}]);

ngApp.controller('CtrlRegister', ['$scope', '$location', function($scope, $location) {
    $scope.registerUser = function() {
        var userObject = {
            'userName' : $scope.ngInputUsername,
            'summonerName' : $scope.ngInputSummonerName,
            'summonerId' : '1111111',
            'summonerIcon' : '121212',
            'emailAddress' : $scope.ngInputEmail,
            'password' : CryptoJS.SHA3($scope.ngInputPassword)
        };

        console.log(userObject);
        debugMsg('User object successfully created.')
    }
}]);

ngApp.controller('CtrlLogin', ['$scope', '$location', function($scope, $location) {
    $scope.login = function() {

    }
}]);