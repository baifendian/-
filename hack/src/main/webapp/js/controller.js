/*首页控制器*/
appModule.controller('indexCtrl', function($scope, $http) {
	/*index data*/
	$http({method:'get', url:'/hack/news.do?method=getindexdata'}).success(function (data) {
		$scope.weather = data.weather;
		// $scope.professionalNews = data.professionalnews;
		// $scope.funnyNews = data.funnynews;
		// $scope.soprtNews = data.sportnews;
		// $scope.moneys = data.managemoney;
	})
	//要闻
	$http({method:'get', url:'/hack/data/importNews.data'}).success(function (data) {
		$scope.importnews = data;
	})
	//行业
	$http({method:'get', url:'/hack/data/professionalNews.data'}).success(function (data) {
		$scope.professionalnews = data;
	})
	//趣闻
	$http({method:'get', url:'/hack/data/funnyNews.data'}).success(function (data) {
		$scope.funnynews = data;
	})
	//体育
	$http({method:'get', url:'/hack/data/sportNews.data'}).success(function (data) {
		$scope.sportnews = data;
	})
	//体育
	$http({method:'get', url:'/hack/data/paramilitaryNews.data'}).success(function (data) {
		$scope.paramilitarynews = data;
	})
	//理财
	$http({method:'get', url:'/hack/data/managemoney.data'}).success(function (data) {
		$scope.moneys = data;
	})

	$scope.gotoDetail = function (netvalue, findate, prdname) {
		var url = "#managingmoneydetail/"+netvalue.replace("%", "")+"&"+findate+"&"+prdname;
		console.log(url);
		window.location.href=url;
	}
});
/*备忘录控制器*/
appModule.controller('reminderCtrl', function($scope, $http) {

});
/*叫餐控制器*/
appModule.controller('takeoutCtrl', function($scope, $http) {
	$http({method:'get', url:'/hack/data/shopinfo.data'}).success(function (data) {
		$scope.shops = data;
	})

	$scope.selforder = function() {
		var maskdiv = $("div.maskdiv");
		var mask = $("div.mask-alert");
		if (maskdiv.hasClass('hide')) {
			maskdiv.removeClass('hide');
			mask.removeClass('hide');
		} else {
			maskdiv.addClass('hide');
			mask.addClass('hide');
		}
	}

	$scope.check = function($event) {
		var a = $("a.classify");
		a.removeClass('active');
		var $this = angular.element($event.target);
		$this.addClass('active');
		return false;
	}

	$scope.order = function(shop) {
		var url = "#takeoutorder/"+shop.shop_name+"&"+shop.average_score+"&"+shop.welfare_info+"&"+shop.takeout_price+"&"+shop.delivery_time+"&"+shop.saled_month;
		window.location.href = url;
	}
});

/*理财控制器*/
appModule.controller('takeoutorderCtrl', function($scope, $http, $routeParams) {
	$scope.shop_name = $routeParams.shop_name;
	$scope.average_score = $routeParams.average_score;
	$scope.welfare_info = $routeParams.welfare_info;
	$scope.takeout_price = $routeParams.takeout_price;
	$scope.delivery_time = $routeParams.delivery_time;
	$scope.saled_month = $routeParams.saled_month;

	$scope.choice = function($event) {
		var other = $("i.radio");
		other.removeClass('active');
		var $this = angular.element($event.target);
		var siradio = $this.siblings('i.radio');
		var niradio = $this.find('i.radio');
		siradio.addClass('active');
		niradio.addClass('active');

	}
});
/*理财控制器*/
appModule.controller('managingmoneyCtrl', function($scope, $http) {
	$http({method:'get', url:'/hack/data/fine.data'}).success(function (data) {
		$scope.data = data;
	})
});
/*理财列表控制器*/
appModule.controller('managingmoneylistCtrl', function($scope, $http) {
	$http({method:'get', url:'/hack/data/managemoneylist.data'}).success(function (data) {
		$scope.data = data;
	})
});

/*理财详情控制器*/
appModule.controller('managingmoneydetailCtrl', function($scope, $http, $routeParams) {
	$scope.netvalue = $routeParams.NetValue;
	$scope.findate = $routeParams.FinDate;
	$scope.prdname = $routeParams.PrdName;
});
/*订单控制器*/
appModule.controller('orderCtrl', function($scope, $http,  $routeParams) {
	$scope.prdname =  $routeParams.prdname;
	$scope.netvalue =  $routeParams.netvalue;
	$scope.findate = $routeParams.findate;
});
/*我的控制器*/
appModule.controller('meCtrl', function($scope, $http) {

});