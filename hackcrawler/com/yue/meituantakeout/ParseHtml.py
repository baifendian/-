# coding=utf-8
'''
Created on 2016年6月28日

@author: BFD_487
'''
import lxml

if __name__ == '__main__':
    html_doc = """
html is:<!DOCTYPE HTML>
<!--[if IE 9]><html class="ie9"><![endif]-->
<!--[if IE 8]><html class="ie8"><![endif]-->
<!--[if IE 7]><html class="ie7"><![endif]-->
<!--[if IE 6]><html class="ie6"><![endif]-->
<!--[if (gt IE 9)|!(IE)]><!--><html><!--<![endif]-->
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link rel="dns-prefetch" href="//xs01.meituan.net">
    <link rel="dns-prefetch" href="//p0.meituan.net">
    <link rel="dns-prefetch" href="//p1.meituan.net">
    
    <meta name="baidu-site-verification" content="Qu9OzfSVVJ" />
    <meta name="keywords" content="外卖,美团外卖,外卖网,外卖网上订餐,美团,美团网">
    <meta name="description" content="美团外卖专业品质外卖网，饿了么，饿了订外卖就上美团外卖。美团外卖覆盖全国各城市优质外卖商家、快餐和特色美食，拥有最先进的外卖网上订餐平台和专业外卖送餐团队，提供24小时叫外卖、外卖网上订餐服务。">
    <title>美团外卖_外卖网_外卖网上订餐_外卖送餐_美团网</title>    <script type="text/javascript">
    var MT = {};
    MT.BOOTSTAMP = new Date().getTime();
    MT.STATIC_ROOT = "http://xs01.meituan.net/waimai_web";
    MT.ENV = "product";
    </script>

    <link rel="shortcut icon" type="image/vnd.microsoft.icon" href="/static/img/favicon_1.ico">
    <link rel="icon" href="/static/img/favicon_1.ico" size="16x16 32x32">

    <link rel="stylesheet" href="http://xs01.meituan.net/waimai_web/css/page/home_0547f15b.css" />


    <script>
      (function(i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] ||
        function() {
          (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o), m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
      })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');
      ga('create', 'UA-45741865-1', {'cookieDomain': 'waimai.meituan.com'});
      ga('send', 'pageview');

      !function(t,e,n){function i(){var t=e.createElement("script");t.async=!0,t.src="//s0.meituan."+(-1===e.location.protocol.indexOf("https")?"net":"com")+"/bs/js/?f=mta-js:mta.min.js";var n=e.getElementsByTagName("script")[0];n.parentNode.insertBefore(t,n)}if(t.MeituanAnalyticsObject=n,t[n]=t[n]||function(){(t[n].q=t[n].q||[]).push(arguments)},"complete"===e.readyState)i();else{var s="addEventListener",r="attachEvent";if(t[s])t[s]("load",i,!1);else if(t[r])t[r]("onload",i);else{var a=t.onload;t.onload=function(){i(),a&&a()}}}}(window,document,"mta"),function(t,e,n){if(e&&!("_mta"in e)){e._mta=!0;var i=t.location.protocol;if("file:"!==i){var s=t.location.host,r=e.prototype.open;e.prototype.open=function(e,n,a,o,h){if(this._method="string"==typeof e?e.toUpperCase():null,n){if(0===n.indexOf("http://")||0===n.indexOf("https://")||0===n.indexOf("//"))this._url=n;else if(0===n.indexOf("/"))this._url=i+"//"+s+n;else{var l=i+"//"+s+t.location.pathname;l=l.substring(0,l.lastIndexOf("/")+1),this._url=l+n}var u=this._url.indexOf("?");-1!==u?(this._searchLength=this._url.length-1-u,this._url=this._url.substring(0,u)):this._searchLength=0}else this._url=null,this._searchLength=0;return this._startTime=(new Date).getTime(),r.apply(this,arguments)};var a="onreadystatechange",o="addEventListener",h=e.prototype.send;e.prototype.send=function(e){function n(n,s){0!==n._url.indexOf(i+"//frep.meituan.net/_.gif")&&t.mta("send","browser.ajax",{url:n._url,method:n._method,error:!(0===n.status.toString().indexOf("2")||304===n.status),responseTime:(new Date).getTime()-n._startTime,requestSize:n._searchLength+(e?e.length:0),responseSize:n.responseText.length})}if(o in this){var s=function(t){n(this,t)};this[o]("load",s),this[o]("error",s),this[o]("abort",s)}else{var r=this[a];this[a]=function(e){r&&r.apply(this,arguments),4===this.readyState&&t.mta&&n(this,e)}}return h.apply(this,arguments)}}}}(window,window.XMLHttpRequest,"mta");
      mta("create","551517ddd0a88b586dc89658");
      mta("send","page");   
    </script>
    </head>
    <body>
      <div class="triffle" id="triffle">
        <div class="stick-qrcode hidden" id="stickQrcode">
          <a class="index-xiaomei qrcode" href="/mobile/download/default" target="_blank">
            <i class="icon i-qrcode-cross"></i>
            <span class="code qrcode"></span>
          </a>
        </div>

        <a href="javascript:;" class="top"><i class="icon i-backtop"></i></a>
        <a id="aside-feedback" target="_blank" href="/help/feedback" class="fb">意见反馈</a>
      </div>
      <div class="wrapper">
          <div id="top-tips" class="top-tips" style="display: none;">
            <a class="j-top-tips-close top-tips-close" href="javascript:;"><i class="icon i-top-tips-close"></i></a>
            <div class="j-top-tips-content top-tips-content" data-id=""></div>
          </div>
        <div class="page-header">
        <div class="top-nav">
          <div class="topnav-wrap">
            <div class="fr welcome">
    <span id="dis-login" class="top-disloginbar fl"><a class="j-register fl" href="http://passport.meituan.com/account/unitivesignup?service=waimai&continue=http%3A%2F%2Fwaimai.meituan.com%3A80%2Faccount%2Fsettoken" rel="nofollow">注册</a><a class="j-login fr" href="http://passport.meituan.com/account/unitivelogin?service=waimai&continue=http%3A%2F%2Fwaimai.meituan.com%3A80%2Faccount%2Fsettoken" rel="nofollow">登录</a>｜ </span>
              <a href="/mobile/download/default" class="wap fl" rel="nofollow"><i class="icon i-top-mobile"></i><span>手机版</span></a>
              <a target="_blank" href="http://meituan.com" class="site-name fl" ><i class="icon i-top-tuan"></i><span>美团网</span></a>
            </div>


            <i class="fl icon i-top-loc"></i>
              <span class="current-city fl" id="current-city">北京</span>
            
            
              
              <span class="address fl" id="address">
                <span id="curr-location" class="current-address fl">北辰世纪中心A座</span>
                <div class="change fl clearfix" id="changePosition">
                  <a href="/?stay=1" class="change-link">
                    <span class="fl">[切换地址]</span>
                  </a>
                </div>
              </span>
            
          </div>
        </div>
        <div class="middle-nav">
          <div class="middlenav-wrap clearfix">
            <h1 class="logo fl">
              <a href="/"  title="美团外卖"><img src="http://xs01.meituan.net/waimai_web/img/logos/normal-new2.png" alt="美团外卖"></a>
            </h1>
            <div class="desire fl">
              <a href="/" class="ca-lightgrey"><span>首页</span></a>
              <span class="vertical-line">|</span>
              <a href="/customer/order/list" class="ca-lightgrey" rel="nofollow"><span>我的外卖</span></a>
              <span class="vertical-line">|</span>
              <a href="/contact/contactus" class="ca-lightgrey"><span>加盟合作</span></a>
            </div>
            <div class="search-box fr">
              <input type="text" class="header-search fl" placeholder="搜索商家，美食" />
              <a href="javascript:;" class="doSearch fr" >搜索</a>
              <div class="result-box">
                <div class="result-left fl">
                  <div class="rest-words ct-black">餐厅</div>
                  <div class="food-words ct-black">美食</div>
                </div>
                <div class="result-right fl">
                  <ul class="rest-lists">
                  </ul>
                  <div class="line"></div>
                  <ul class="food-lists">
                  </ul>
                </div>
              </div>
              <div class="no-result">
                没有找到相关结果，请换个关键字搜索！
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="page-wrap">
        <div class="inner-wrap">



  






<script type="text/javascript">
  var FIRST_HAS_MORE = Boolean("true");
</script>

<script id="page-data-template" type="text/template">
  {"page":  "home"
  }
  </script>

<div class="inner-bg">

  

    <div class="rest-banner">
      <div class="imgsort-wrapper">
        <span class="imgsort-filter-title">商家分类</span>
        <ul class="clearfix imgsort-content">
          <li class="fl selected">
            <a href="javascript:void(0);" data-cate="cate_all" class="imgsort-list" title="全部">
              <span class="imgsort-info">全部</span>
            </a>
          </li>
            <li class="fl ">
              <a class="imgsort-list" title="鲜花绿植" href="javascript:void(0);" data-cate="cate_1001">
                <span class="imgsort-info">鲜花绿植</span>
              </a>
            </li>
            <li class="fl ">
              <a class="imgsort-list" title="美食" href="javascript:void(0);" data-cate="cate_1000">
                <span class="imgsort-info">美食</span>
              </a>
            </li>
            <li class="fl ">
              <a class="imgsort-list" title="甜点饮品" href="javascript:void(0);" data-cate="cate_19">
                <span class="imgsort-info">甜点饮品</span>
              </a>
            </li>
            <li class="fl ">
              <a class="imgsort-list" title="生鲜果蔬" href="javascript:void(0);" data-cate="cate_21">
                <span class="imgsort-info">生鲜果蔬</span>
              </a>
            </li>
            <li class="fl ">
              <a class="imgsort-list" title="生活超市" href="javascript:void(0);" data-cate="cate_20">
                <span class="imgsort-info">生活超市</span>
              </a>
            </li>
            <li class="fl">
              <a class="imgsort-list" title="药品" href="/drugs/drug?category_code=0">
                <span class="imgsort-info">药品</span>
              </a>
            </li>
        </ul>
      </div>
        <div class="rest-filter clearfix">
          <span class="rest-filter-title">优惠筛选</span>
                <!--  -->
              <a title="下单立减" href="javascript:void(0);" data-rest="fulldiscount">
                <span class="sprite checkbox"></span>
                <span class="txt">    下单立减
    
</span>
              </a>
                <!--  -->
              <a title="赠300ml可乐、雪碧或芬达" href="javascript:void(0);" data-rest="mealsdonation_4">
                <span class="sprite checkbox"></span>
                <span class="txt">    赠300m
    ...
</span>
              </a>
                <!--  -->
              <a title="赠310ml加多宝" href="javascript:void(0);" data-rest="mealsdonation_18">
                <span class="sprite checkbox"></span>
                <span class="txt">    赠310m
    ...
</span>
              </a>
                <!--  -->
              <a title="可用抵价券" href="javascript:void(0);" data-rest="coupondiscount">
                <span class="sprite checkbox"></span>
                <span class="txt">    可用抵价券
    
</span>
              </a>
                <!--  -->
              <a title="下单赠饮料" href="javascript:void(0);" data-rest="fulldonation">
                <span class="sprite checkbox"></span>
                <span class="txt">    下单赠饮料
    
</span>
              </a>
                <!--  -->
              <a title="新用户优惠" href="javascript:void(0);" data-rest="firstdiscount">
                <span class="sprite checkbox"></span>
                <span class="txt">    新用户优惠
    
</span>
              </a>
                <!--  -->
              <a title="提前下单优惠" href="javascript:void(0);" data-rest="inadvance">
                <span class="sprite checkbox"></span>
                <span class="txt">    提前下单优
    ...
</span>
              </a>
                <!--  -->
              <a title="超时赔付" href="javascript:void(0);" data-rest="compensate">
                <span class="sprite checkbox"></span>
                <span class="txt">    超时赔付
    
</span>
              </a>
                <!--  -->
              <a title="支持发票" href="javascript:void(0);" data-rest="invoice">
                <span class="sprite checkbox"></span>
                <span class="txt">    支持发票
    
</span>
              </a>

            <a title="在线支付" href="javascript:void(0);" data-rest="online_pay">
              <span class="sprite checkbox "></span>
              <span class="txt">在线支付</span>
            </a>


            <a title="美团专送" href="javascript:void(0);" data-rest="logistic">
              <span class="sprite checkbox "></span>
              <span class="txt">美团专送</span>
            </a>
        </div>
      <div class="divider"></div>
      <div class="sort-filter" id="sortFilter">
        <a class="sort default-sort active" data-sort="0" href="javascript:void(0);">默认排序</a>
        <a class="sort sa-sort" data-sort="1" href="javascript:void(0);">销量<i class="icon i-orderdown"></i></a>
        <a class="sort ct-sort" data-sort="2" href="javascript:void(0);">评价<i class="icon i-orderdown"></i></a>
        <a class="sort ti-sort" data-sort="3" href="javascript:void(0);">送餐速度<i class="icon i-orderup"></i></a>
        <div class="fl clearfix">
          <span class="fl label">起送价筛选</span>
          <div class="prices">
            <a class="all" href="javascript:;">
              全部商家<i class="icon i-triangle-dn"></i>
            </a>
            <ul>
              <li><a data-price="0" href="javascript:void(0);">全部商家</a></li>
              <li><a data-price="1" href="javascript:void(0);">10元以下</a></li>
              <li><a data-price="2" href="javascript:void(0);">20元以下</a></li>
              <li><a data-price="3" href="javascript:void(0);">30元以下</a></li>
            </ul>
          </div>
        </div>
         
              </div>
    </div>
  <div class="rest-list">
    <ul class="list clearfix">
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="安逸串吧" data-bulletin="" data-poiid="312532" class="restaurant" data-all="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
        data-minpricelevel="5">
        <a class="rest-atag" href="/restaurant/312532?pos=0" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="312532" data-index="0" class="scroll-loading" src="http://p0.meituan.net/xianfu/a8b1c7d312129a1e22d460162e1cbe6720540.jpg" data-src="http://p0.meituan.net/xianfu/a8b1c7d312129a1e22d460162e1cbe6720540.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="安逸串吧">
    安逸串吧
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 68px"></span>
                  </span>
                  <span class="score-num fl">4.6分</span>
                  <span class="total cc-lightred-new fr">
月售446单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥50</span>
                <span class="send-price">
                  免配送费
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      34分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家��持在线支付</script>

              <!-- 是否支持代金券 -->





                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减12元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满50元减1元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="312532" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="拼豆夜宵（亚运村店）" data-bulletin="拼豆夜宵，北京夜宵连锁领导品牌，北京全城多家门店，1小时内保温配送。主营：港式点心，香辣海鲜，特色火锅，经典西餐，甜品小菜，酒水零食，应急日用等。 拼豆夜宵，只为满足深夜的那份渴望！" data-poiid="765226" class="restaurant" data-all="1"
            data-invoice="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
        data-minpricelevel="3">
        <a class="rest-atag" href="/restaurant/765226?pos=1" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="765226" data-index="1" class="scroll-loading" src="http://p1.meituan.net/xianfu/d5adbdef4609f4f1d686be8522b82fb76144.jpg" data-src="http://p1.meituan.net/xianfu/d5adbdef4609f4f1d686be8522b82fb76144.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="拼豆夜宵（亚运村店）">
    拼豆夜宵（亚运村店）
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 69px"></span>
                  </span>
                  <span class="score-num fl">4.7分</span>
                  <span class="total cc-lightred-new fr">
月售1220单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥30</span>
                <span class="send-price">
                  配送费:￥9
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      35分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->



                  <i class="icon i-cheque"></i>
                <script type="text/template" data-icon="i-cheque">支持开发票，开票金额150元起。请在下单时填好发票抬头。默认手撕发票，如需机打请备注抬头与联系方式，我们将邮寄给您</script>


                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减14元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满60元减10元;满80元减20元;满100元减30元;满200元减65元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="765226" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="熊小递" data-bulletin="熊小递全新开启味美、价廉、品质新篇章，感谢您的关注与监督   客服电话：17080036007" data-poiid="651659" class="restaurant" data-all="1"
            data-invoice="1"
            data-fulldonation="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
        data-minpricelevel="5">
        <a class="rest-atag" href="/restaurant/651659?pos=2" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="651659" data-index="2" class="scroll-loading" src="http://p0.meituan.net/xianfu/4b5a995d8d38d93f109b6226a4a310fb83968.jpg" data-src="http://p0.meituan.net/xianfu/4b5a995d8d38d93f109b6226a4a310fb83968.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="熊小递">
    熊小递
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 67px"></span>
                  </span>
                  <span class="score-num fl">4.6分</span>
                  <span class="total cc-lightred-new fr">
月售779单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥20</span>
                <span class="send-price">
                  配送费:￥2
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      34分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->



                  <i class="icon i-cheque"></i>
                <script type="text/template" data-icon="i-cheque">支持开发票，开票金额100元起。请在下单时填好发票抬头。麻烦备注好抬头，辛苦啦</script>

                  <i class="icon i-free-gift"></i>
                <script type="text/template" data-icon="i-free-gift">
                  每单满50元赠送加多宝<span class="special">(手机客户端专享)</span>
                </script>

                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减12元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满20元减6元;满50元减15元;满100元减30元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="651659" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="爱尚炸鸡店" data-bulletin="" data-poiid="917780" class="restaurant" data-all="1"
            data-fulldonation="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
        data-minpricelevel="12">
        <a class="rest-atag" href="/restaurant/917780?pos=3" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="917780" data-index="3" class="scroll-loading" src="http://p1.meituan.net/xianfu/ee422f3ec53a73b407f6d4e31099d718284727.jpg" data-src="http://p1.meituan.net/xianfu/ee422f3ec53a73b407f6d4e31099d718284727.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="爱尚炸鸡店">
    爱尚炸鸡店
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 69px"></span>
                  </span>
                  <span class="score-num fl">4.8分</span>
                  <span class="total cc-lightred-new fr">
月售1580单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥70</span>
                <span class="send-price">
                  配送费:￥2
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      31分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->




                  <i class="icon i-free-gift"></i>
                <script type="text/template" data-icon="i-free-gift">
                  每单满80元赠送大可乐<span class="special">(手机客户端专享)</span>
                </script>

                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减12元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满30元减10元;满50元减16元;满100元减26元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="917780" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
          <li class="rest-separate j-rest-separate"></li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="炸鸡啤酒（亚运村店）" data-bulletin="亲，有任何问题都可以致电我们哟！给您一个满意答复！如果您评价的话，我们在寻找您的单子，耽误了一定的时间，直接给我们打电话，问题一下就OK啦！" data-poiid="823624" class="restaurant" data-all="1"
            data-fulldonation="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
            data-inadvance="1"
        data-minpricelevel="11">
        <a class="rest-atag" href="/restaurant/823624?pos=4" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="823624" data-index="4" class="scroll-loading" src="http://p1.meituan.net/xianfu/e0b7ffe2d87867b57fbfb2c63f2b9c6c43008.jpg" data-src="http://p1.meituan.net/xianfu/e0b7ffe2d87867b57fbfb2c63f2b9c6c43008.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="炸鸡啤酒（亚运村店）">
    炸鸡啤酒（亚运村店）
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 70px"></span>
                  </span>
                  <span class="score-num fl">4.8分</span>
                  <span class="total cc-lightred-new fr">
月售854单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥88</span>
                <span class="send-price">
                  配送费:￥15
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      36分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->




                  <i class="icon i-free-gift"></i>
                <script type="text/template" data-icon="i-free-gift">
                  每单满99元赠送进口啤酒<span class="special">(手机客户端专享)</span>
                </script>

                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减24元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满30元减8元;满60元减16元;满100元减20元<span class="special">(手机客户端专享)</span>
                  
                </script>


                  <i class="icon i-ding"></i>
                <script type="text/template" data-icon="i-ding">
                  16:00-19:00下单减1元<span class="special">(手机客户端专享)</span>
                </script>






            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="823624" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="全时美食" data-bulletin="" data-poiid="906676" class="restaurant" data-all="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
        data-minpricelevel="1">
        <a class="rest-atag" href="/restaurant/906676?pos=5" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="906676" data-index="5" class="scroll-loading" src="http://p1.meituan.net/xianfu/113d59d6ab3b632303533e42dd7ecc2b248363.jpg" data-src="http://p1.meituan.net/xianfu/113d59d6ab3b632303533e42dd7ecc2b248363.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="全时美食">
    全时美食
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 65px"></span>
                  </span>
                  <span class="score-num fl">4.4分</span>
                  <span class="total cc-lightred-new fr">
月售230单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥0</span>
                <span class="send-price">
                  免配送费
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      48分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->





                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减11元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满20元减8元;满30元减11元;满60元减20元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="906676" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="极速食客" data-bulletin="本店接受公司学校团餐预定！团餐预订电话15313165951。
餐厅电话17710306884" data-poiid="12721" class="restaurant" data-all="1"
            data-invoice="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
        data-minpricelevel="16">
        <a class="rest-atag" href="/restaurant/12721?pos=6" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="12721" data-index="6" class="scroll-loading" src="http://p1.meituan.net/xianfu/c5f3079697b2659185f064097b2a7e13237434.jpg" data-src="http://p1.meituan.net/xianfu/c5f3079697b2659185f064097b2a7e13237434.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="极速食客">
    极速食客
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 68px"></span>
                  </span>
                  <span class="score-num fl">4.6分</span>
                  <span class="total cc-lightred-new fr">
月售6079单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥85</span>
                <span class="send-price">
                  配送费:￥9
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      38分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->



                  <i class="icon i-cheque"></i>
                <script type="text/template" data-icon="i-cheque">支持开发票，开票金额50元起。请在下单时填好发票抬头。</script>


                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减19元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满25元减12元;满50元减19元;满100元减22元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="12721" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="井号夜宵（亚运村店）" data-bulletin="" data-poiid="1083176" class="restaurant" data-all="1"
            data-fulldiscount="1"
        data-minpricelevel="3">
        <a class="rest-atag" href="/restaurant/1083176?pos=7" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="1083176" data-index="7" class="scroll-loading" src="http://p0.meituan.net/xianfu/d3a1832ab11c6953167e18d464576f06193336.jpg" data-src="http://p0.meituan.net/xianfu/d3a1832ab11c6953167e18d464576f06193336.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="井号夜宵（亚运村店）">
    井号夜宵（亚运村店）
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 75px"></span>
                  </span>
                  <span class="score-num fl">5.0分</span>
                  <span class="total cc-lightred-new fr">
月售32单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥30</span>
                <span class="send-price">
                  配送费:￥8
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      44分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->






                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满30元减15元;满50元减10元;满100元减25元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="1083176" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
          <li class="rest-separate j-rest-separate"></li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="沙家辣鸭脖" data-bulletin="" data-poiid="72724" class="restaurant" data-all="1"
            data-invoice="1"
            data-firstdiscount="1"
        data-minpricelevel="26">
        <a class="rest-atag" href="/restaurant/72724?pos=8" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="72724" data-index="8" class="scroll-loading" src="http://p0.meituan.net/xianfu/2db00b47d8144be9de9ce781fdad9164403936.jpg" data-src="http://p0.meituan.net/xianfu/2db00b47d8144be9de9ce781fdad9164403936.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="沙家辣鸭脖">
    沙家辣鸭脖
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 66px"></span>
                  </span>
                  <span class="score-num fl">4.5分</span>
                  <span class="total cc-lightred-new fr">
月售303单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥50</span>
                <span class="send-price">
                  配送费:￥30
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      35分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->



                  <i class="icon i-cheque"></i>
                <script type="text/template" data-icon="i-cheque">支持开发票，开票金额100元起。请在下单时填好发票抬头。需要发票提前说明</script>


                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减11元<span class="special">(手机客户端专享)</span></script>









            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="72724" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="经贸串吧（韩式炸鸡）" data-bulletin="本店新添韩式炸鸡类美食，欢迎新老客户品评" data-poiid="180356" class="restaurant" data-all="1"
            data-fulldonation="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
            data-inadvance="1"
        data-minpricelevel="6">
        <a class="rest-atag" href="/restaurant/180356?pos=9" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="180356" data-index="9" class="scroll-loading" src="http://p1.meituan.net/xianfu/d77eddfbb65d475a9e16d1279ab146ed365024.jpg" data-src="http://p1.meituan.net/xianfu/d77eddfbb65d475a9e16d1279ab146ed365024.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="经贸串吧（韩式炸鸡）">
    经贸串吧（韩式炸鸡）
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 66px"></span>
                  </span>
                  <span class="score-num fl">4.5分</span>
                  <span class="total cc-lightred-new fr">
月售417单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥60</span>
                <span class="send-price">
                  免配送费
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      47分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->




                  <i class="icon i-free-gift"></i>
                <script type="text/template" data-icon="i-free-gift">
                  每单满150元赠送大可乐<span class="special">(手机客户端专享)</span>
                </script>

                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减12元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满35元减5元;满60元减10元;满100元减20元<span class="special">(手机客户端专享)</span>
                  
                </script>


                  <i class="icon i-ding"></i>
                <script type="text/template" data-icon="i-ding">
                  07:00-10:00下单减1元;14:00-17:00下单减1元<span class="special">(手机客户端专享)</span>
                </script>






            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="180356" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="约克比萨" data-bulletin="1:本餐厅奶酪选自纯进口新西兰安佳奶酪，其他食材节选自味好    美，荷美尔等知名品牌请放心食用。
2：本餐厅的企业文化核心是微利走心，所以用餐高峰期堂食和外卖都很多，以至于我们无法保证 每一份外卖都能准时送达，餐厅上下会利用一切资源竭尽所能尽快送到亲们的手中，感谢您的惠顾和理解!" data-poiid="85064" class="restaurant" data-all="1"
            data-invoice="1"
            data-coupondiscount="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
        data-minpricelevel="8">
        <a class="rest-atag" href="/restaurant/85064?pos=10" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="85064" data-index="10" class="scroll-loading" src="http://p1.meituan.net/xianfu/__43635697__4783889.jpg" data-src="http://p1.meituan.net/xianfu/__43635697__4783889.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="约克比萨">
    约克比萨
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 66px"></span>
                  </span>
                  <span class="score-num fl">4.5分</span>
                  <span class="total cc-lightred-new fr">
月售1282单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥30</span>
                <span class="send-price">
                  配送费:￥3
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      37分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支��</script>

              <!-- 是否支持代金券 -->
                  <i class="icon i-ticket"></i>
                <script type="text/template" data-icon="i-ticket">该餐厅支持使用代金券<span class="special">(手机客户端专享)</span></script>



                  <i class="icon i-cheque"></i>
                <script type="text/template" data-icon="i-cheque">支持开发票，开票金额50元起。请在下单时填好发票抬头。</script>


                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减15元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满20元减7元;满45元减11元;满65元减15元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="85064" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="食道乐韩式炸鸡" data-bulletin="" data-poiid="870735" class="restaurant" data-all="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
        data-minpricelevel="14">
        <a class="rest-atag" href="/restaurant/870735?pos=11" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="870735" data-index="11" class="scroll-loading" src="http://p1.meituan.net/xianfu/56ed89c4460ac4ec728cf3e7b35440f680190.jpg" data-src="http://p1.meituan.net/xianfu/56ed89c4460ac4ec728cf3e7b35440f680190.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="食道乐韩式炸鸡">
    食道乐韩式炸鸡
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 70px"></span>
                  </span>
                  <span class="score-num fl">4.8分</span>
                  <span class="total cc-lightred-new fr">
月售127单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥115</span>
                <span class="send-price">
                  配送费:￥2
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      50+分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->





                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减12元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满30元减6元;满60元减12元;满110元减30元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="870735" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
          <li class="rest-separate j-rest-separate"></li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="江依林韩式快餐烤串吧（五道口店）" data-bulletin="【本店只接受在线支付】（因本店串类口味较多，请您下单时注意选择好口味，甜辣的串烤不了不辣 ）建议周四五六晚上19：00以后定餐的请提前一小时下单订餐。实体店位于五道口王庄路东王庄小区33号楼。" data-poiid="868496" class="restaurant" data-all="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
        data-minpricelevel="15">
        <a class="rest-atag" href="/restaurant/868496?pos=12" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="868496" data-index="12" class="scroll-loading" src="http://p1.meituan.net/xianfu/b68da06d26150d7eab24320d91008684154538.jpg" data-src="http://p1.meituan.net/xianfu/b68da06d26150d7eab24320d91008684154538.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="江依林韩式快餐烤串吧（五道口店）">
    江依林韩式快餐烤串吧（
    ...
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 69px"></span>
                  </span>
                  <span class="score-num fl">4.8分</span>
                  <span class="total cc-lightred-new fr">
月售957单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥60</span>
                <span class="send-price">
                  配送费:￥6
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      33分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->





                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减12元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满60元减5元;满100元减10元;满150元减15元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="868496" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="三月蛋糕" data-bulletin="草莓已经来货，欢迎大家尽情选购！三月蛋糕与您相伴，" data-poiid="965672" class="restaurant" data-all="1"
            data-invoice="1"
            data-fulldonation="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
            data-inadvance="1"
        data-minpricelevel="2">
        <a class="rest-atag" href="/restaurant/965672?pos=13" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="965672" data-index="13" class="scroll-loading" src="http://p1.meituan.net/xianfu/a2162e8d78124656cf3584ff4c11df83558738.jpg" data-src="http://p1.meituan.net/xianfu/a2162e8d78124656cf3584ff4c11df83558738.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="三月蛋糕">
    三月蛋糕
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 70px"></span>
                  </span>
                  <span class="score-num fl">4.8分</span>
                  <span class="total cc-lightred-new fr">
月售231单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥0</span>
                <span class="send-price">
                  免配送费
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      50+分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->



                  <i class="icon i-cheque"></i>
                <script type="text/template" data-icon="i-cheque">支持开发票，开票金额120元起。请在下单时填好发票抬头。</script>

                  <i class="icon i-free-gift"></i>
                <script type="text/template" data-icon="i-free-gift">
                  每单满90元赠送面包1份<span class="special">(手机客户端专享)</span>
                </script>

                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减29元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满158元减40元;满200元减80元;满300元减120元<span class="special">(手机客户端专享)</span>
                  
                </script>


                  <i class="icon i-ding"></i>
                <script type="text/template" data-icon="i-ding">
                  09:00-11:00下单减5元;14:00-18:00下单减5元<span class="special">(手机客户端专享)</span>
                </script>






            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="965672" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="哈哈镜（外馆斜街店）" data-bulletin="订购有优惠" data-poiid="609835" class="restaurant" data-all="1"
            data-fulldonation="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
        data-minpricelevel="5">
        <a class="rest-atag" href="/restaurant/609835?pos=14" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="609835" data-index="14" class="scroll-loading" src="http://p0.meituan.net/xianfu/e6493702945d485a0211ce5a36c37c91140424.jpg" data-src="http://p0.meituan.net/xianfu/e6493702945d485a0211ce5a36c37c91140424.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="哈哈镜（外馆斜街店）">
    哈哈镜（外馆斜街店）
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 70px"></span>
                  </span>
                  <span class="score-num fl">4.8分</span>
                  <span class="total cc-lightred-new fr">
月售280单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥50</span>
                <span class="send-price">
                  配送费:￥7
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      27分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->




                  <i class="icon i-free-gift"></i>
                <script type="text/template" data-icon="i-free-gift">
                  每单满100元赠送随机发放2份（荤）<span class="special">(手机客户端专享)</span>
                </script>

                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减12元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满30元减3元;满50元减5元;满80元减10元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="609835" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="食牛族私房牛肉外卖" data-bulletin="晚00点后每单加收10元夜间配送费 快递员上门收取
本店所有菜品照片均为实物拍摄
现场制作 订单较多 请提前一个半小时下单 
北京全城配送 订餐电话：13552520332
微信：snz010" data-poiid="312373" class="restaurant" data-all="1"
            data-invoice="1"
            data-fulldonation="1"
            data-fulldiscount="1"
            data-inadvance="1"
        data-minpricelevel="10">
        <a class="rest-atag" href="/restaurant/312373?pos=15" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="312373" data-index="15" class="scroll-loading" src="http://p0.meituan.net/xianfu/a5e1e43bb8068544f55c6bf39f14e41f66199.jpg" data-src="http://p0.meituan.net/xianfu/a5e1e43bb8068544f55c6bf39f14e41f66199.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="食牛族私房牛肉外卖">
    食牛族私房牛肉外卖
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 68px"></span>
                  </span>
                  <span class="score-num fl">4.7分</span>
                  <span class="total cc-lightred-new fr">
月售729单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥30</span>
                <span class="send-price">
                  配送费:￥15
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      50+分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->



                  <i class="icon i-cheque"></i>
                <script type="text/template" data-icon="i-cheque">支持开发票，开票金额300元起。请在下单时填好发票抬头。300元起开发票，一周内送到</script>

                  <i class="icon i-free-gift"></i>
                <script type="text/template" data-icon="i-free-gift">
                  每单满200元赠送龙徽赤霞珠干红葡萄酒1瓶<span class="special">(手机客户端专享)</span>
                </script>


                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满25元减9元;满100元减13元;满200元减16元<span class="special">(手机客户端专享)</span>
                  
                </script>


                  <i class="icon i-ding"></i>
                <script type="text/template" data-icon="i-ding">
                  09:00-11:00下单减1元;14:00-16:00下单减1元<span class="special">(手机客户端专享)</span>
                </script>






            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="312373" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
          <li class="rest-separate j-rest-separate"></li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="壹加壹炸鸡" data-bulletin="" data-poiid="553804" class="restaurant" data-all="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
        data-minpricelevel="8">
        <a class="rest-atag" href="/restaurant/553804?pos=16" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="553804" data-index="16" class="scroll-loading" src="http://p0.meituan.net/xianfu/b16821ee3a722b5da11c8ba22e64b8a2304395.jpg" data-src="http://p0.meituan.net/xianfu/b16821ee3a722b5da11c8ba22e64b8a2304395.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="壹加壹炸鸡">
    壹加壹炸鸡
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 69px"></span>
                  </span>
                  <span class="score-num fl">4.8分</span>
                  <span class="total cc-lightred-new fr">
月售747单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥80</span>
                <span class="send-price">
                  配送费:￥8
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      38分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->





                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减12元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满40元减4元;满70元减12元;满110元减20元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="553804" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="好哥们夜宵" data-bulletin="本店深夜为您觅寻各地美食，送达速度快。还有小惊喜" data-poiid="642626" class="restaurant" data-all="1"
            data-fulldonation="1"
            data-firstdiscount="1"
            data-fulldiscount="1"
            data-inadvance="1"
        data-minpricelevel="6">
        <a class="rest-atag" href="/restaurant/642626?pos=17" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="642626" data-index="17" class="scroll-loading" src="http://p0.meituan.net/xianfu/bac3a54ebf8147cb42fd60e816ac2f02426245.jpg" data-src="http://p0.meituan.net/xianfu/bac3a54ebf8147cb42fd60e816ac2f02426245.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="好哥们夜宵">
    好哥们夜宵
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 60px"></span>
                  </span>
                  <span class="score-num fl">4.0分</span>
                  <span class="total cc-lightred-new fr">
月售48单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥58</span>
                <span class="send-price">
                  配送费:￥7
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      44分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->




                  <i class="icon i-free-gift"></i>
                <script type="text/template" data-icon="i-free-gift">
                  每单满100元赠送2L大可乐<span class="special">(手机客户端专享)</span>
                </script>

                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减13元<span class="special">(手机客户端专享)</span></script>

                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满80元减10元;满100元减20元<span class="special">(手机客户端专享)</span>
                  
                </script>


                  <i class="icon i-ding"></i>
                <script type="text/template" data-icon="i-ding">
                  07:00-13:00下单减1元;14:00-19:00下单减1元<span class="special">(手机客���端专享)</span>
                </script>






            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="642626" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="麻辣诱惑·麻辣小龙虾·麻小外卖" data-bulletin="营业时间：10:00至次日2：30
外送费用：20元外送费
起送价： 0元起送
送餐时间：59分钟" data-poiid="19177" class="restaurant" data-all="1"
            data-invoice="1"
            data-firstdiscount="1"
        data-minpricelevel="1">
        <a class="rest-atag" href="/restaurant/19177?pos=18" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="19177" data-index="18" class="scroll-loading" src="http://p1.meituan.net/xianfu/79fbcfa923f7cc97e0b1ca86e79340f618432.jpg" data-src="http://p1.meituan.net/xianfu/79fbcfa923f7cc97e0b1ca86e79340f618432.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="麻辣诱惑·麻辣小龙虾·麻小外卖">
    麻辣诱惑·麻辣小龙虾·
    ...
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 70px"></span>
                  </span>
                  <span class="score-num fl">4.9分</span>
                  <span class="total cc-lightred-new fr">
月售8432单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥0</span>
                <span class="send-price">
                  配送费:￥20
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      50+分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->



                  <i class="icon i-cheque"></i>
                <script type="text/template" data-icon="i-cheque">支持开发票，开票金额0元起。请在下单时填好发票抬头。</script>


                  <i class="icon i-first"></i>
                <script type="text/template" data-icon="i-first">新用户首次下单,立减14元<span class="special">(手机客户端专享)</span></script>









            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="19177" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
        <li class="fl rest-li" >    <div class="j-rest-outer rest-outer transition ">
      <div data-title="六婆炸鸡" data-bulletin="" data-poiid="712064" class="restaurant" data-all="1"
            data-fulldiscount="1"
        data-minpricelevel="15">
        <a class="rest-atag" href="/restaurant/712064?pos=19" target="_blank">
          <div class="top-content">
            <div class="preview">
              <img data-rid="712064" data-index="19" class="scroll-loading" src="http://p0.meituan.net/xianfu/d0f871a38d40d3e27da725be004583a794208.jpg" data-src="http://p0.meituan.net/xianfu/d0f871a38d40d3e27da725be004583a794208.jpg" data-max-width="208" data-max-height="156"  />
              <div class="rest-tags">
              </div>
            </div>
            <div class="content">
              <div class="name">
                <span title="六婆炸鸡">
    六婆炸鸡
    
                </span>
              </div>
                <div class="rank clearfix">
                  <span class="star-ranking fl">
                    <!-- 5颗星60px长度，算此时星级的长度 -->
                    <!-- 算出空白填充的部分长度 -->
                    <span class="star-score" style="width: 61px"></span>
                  </span>
                  <span class="score-num fl">4.1分</span>
                  <span class="total cc-lightred-new fr">
月售93单
                  </span>
                </div>
              <div class="price">
                <span class="start-price">起送:￥100</span>
                <span class="send-price">
                  配送费:￥5
                </span>
                <span class="send-time"><i class="icon i-poi-timer"></i>
                      50+分钟
                </span>
              </div>
            </div>
            <div class="clear"></div>
          </div>
          <div class="others">
            <div class="discount">

                  <i class="icon i-pay"></i>
                <script type="text/template" data-icon="i-pay">该商家支持在线支付</script>

              <!-- 是否支持代金券 -->






                  <i class="icon i-minus"></i>
                <script type="text/template" data-icon="i-minus">
                  满35元减7元;满70元减15元;满100元减25元<span class="special">(手机客户端专享)</span>
                  
                </script>








            </div>
          </div>
        </a>
          <a href="javascript:;" class="un-favorite j-save-up" data-poiid="712064" title="收藏商家">
            <i class="icon i-poi-fav1"></i>
          </a>
      </div>
    </div>
</li>
    </ul>
  </div>



</div>

      </div>
    </div>
    <div class="page-footer">
      <div class="footer-wrap">
        <div class="column fl help">
          <div class="title">用户帮助</div>
          <ul>
            <li><a href="/help/faq" class="ca-darkgrey" target="_blank" rel="nofollow">常见问题</a></li>
            <li><a href="/help/feedback" class="ca-darkgrey" target="_blank" rel="nofollow">用户反馈</a></li>
            <li><a href="/help/inform" class="ca-darkgrey" target="_blank" rel="nofollow">诚信举报</a></li>
            <li><a href="/restaurant/0" class="ca-darkgrey" target="_blank" rel="nofollow">线上体验店</a></li>
          </ul>
        </div>
        <div class="column fl update">
          <div class="title">获取更新</div>
          <ul>
            <li><a href="/mobile/download/default" class="ca-darkgrey" target="_blank" rel="nofollow">iPhone/Android</a></li>
            <li><a href="http://e.weibo.com/u/3949575070" class="ca-darkgrey" target="_blank" rel="nofollow">美团外卖新浪微博</a></li>
            <li><span class="ct-darkgrey">公众微信号：美团外卖</span></li>
          </ul>
        </div>
        <div class="column fl corp">
          <div class="title">商务合作</div>
          <ul>
            <li><a href="http://kaidian.waimai.meituan.com/open_store/welcome?source=1" class="ca-darkgrey kaidian_address" target="_blank" rel="nofollow">我要开店</a></li>
            <li><a href="/help/banma" class="ca-darkgrey" target="_blank" rel="nofollow">配送合作申请入口</a></li>
            <li><a href="/help/agent" class="ca-darkgrey" target="_blank" rel="nofollow">城市代理商申请入口</a></li>
          </ul>
        </div>
        <div class="column fl info">
          <div class="title">公司信息</div>
          <ul>
            <li><a href="http://www.meituan.com/about/" class="ca-darkgrey" target="_blank" rel="nofollow">关于美团</a></li>
            <li><a href="http://www.meituan.com/about/press" class="ca-darkgrey" target="_blank" rel="nofollow">媒体报道</a></li>
            <li><a href="/help/job" class="ca-darkgrey" target="_blank" rel="nofollow">加入我们</a></li>
          </ul>
        </div>
        <div class="column fr service">
          <div><i class="icon i-service-avatar" ></i></div>
          <div class="details">
            <p class="w1">美团外卖客服电话</p>
            <p class="w2">10109777</p>
            <!-- <p class="w2">4008508888</p> -->
            <!-- <p class="w2">010-56652722</p> -->

              <p class="w3">周一到周日 9:00-23:00</p>

            <p class="w3">客服不受理商务合作</p>
          </div>
        </div>
        <div class="clear"></div>
        <div class="copyright">&copy;2015 meituan.com <a target="_blank" href="http://www.miibeian.gov.cn/">京ICP证070791号</a> 京公网安备11010502025545号</div>
        <div class="sp-ft">
          <a target="_blank" title="备案信息" href="http://www.hd315.gov.cn/beian/view.asp?bianhao=010202011122700003" class="record"></a>
        </div>
      </div>
    </div>
  </div>

    <script type="text/javascript" data-main="http://xs01.meituan.net/waimai_web/js/page/home_b187e86f" src="http://xs01.meituan.net/waimai_web/js/lib/r.js"></script>

    </body>
</html>
"""
