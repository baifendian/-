var appModule = angular.module('mainApp', ['ngRoute']).config(
	[ '$routeProvider', function($routeProvider) {
		$routeProvider.when('/index',
			{
				controller : 'indexCtrl',
				templateUrl : 'views/lifeboom.html'
				// template : "index"
			}
		)
		.when('/reminder',
			{
				controller : 'reminderCtrl',
				templateUrl : 'views/reminder.html'
				// template : "reminder"
			}
		)
		.when('/takeout', 
			{
				controller : 'takeoutCtrl',
				templateUrl : 'views/takeout.html'
			}
		)
		.when('/takeoutorder/:shop_name&:average_score&:welfare_info&:takeout_price&:delivery_time&:saled_month', 
			{
				controller : 'takeoutorderCtrl',
				templateUrl : 'views/takeoutorder.html'
			}
		)
		.when('/managingmoney',
			{
				controller : 'managingmoneyCtrl',
				templateUrl : 'views/managingmoney.html'
				// template : "managinmoney"
			}
		)
		.when('/managingmoneylist',
			{
				controller : 'managingmoneylistCtrl',
				templateUrl : 'views/managingmoneylist.html'
				// template : "managinmoneylist"
			}
		)
		.when('/managingmoneydetail/:NetValue&:FinDate&:PrdName', 
			{
				controller : 'managingmoneydetailCtrl',
				templateUrl : 'views/managingmoneydetail.html'
				// template : "managinmoneydetail"
			}
		)
		.when('/order/:prdname&:netvalue&:findate', 
			{
				controller : 'orderCtrl',
				templateUrl : 'views/order.html'
				// template : "order"
			}
		)
		.when('/me',
			{	
				controller : "meCtrl",
				templateUrl:'views/me.html'
			}
		)
		.otherwise(
			{
				redirectTo:'/index'
			}
		);
	}]
);

appModule.filter("removepercent", function() {
	return function(input) {
		return input.replace('%', '');
	}
})

appModule.filter("substr", function() {
	return function(input) {
		return input[1] + " ..."; 
	}
})


// angular.module('ng').filter('cut', function () {
//   return function (value, wordwise, max, tail) {
//     if (!value) return '';

//     max = parseInt(max, 10);
//     if (!max) return value;
//     if (value.length <= max) return value;

//     value = value.substr(0, max);
//     if (wordwise) {
//       var lastspace = value.lastIndexOf(' ');
//       if (lastspace != -1) {
//         value = value.substr(0, lastspace);
//       }
//     }

//     return value + (tail || ' …');
//   };
// });