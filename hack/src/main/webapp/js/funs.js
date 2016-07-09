/**
 * Created by haomei on 2015/7/21.
 */
$(document).ready(function(){
    $("nav a").click(function(){
        var index=$(this).index();
        $(".taggle").hide().eq(index).show();
        $("nav a").removeClass("active");
        $("nav a").eq(index).addClass('active');
    })

    /*产品详情伸缩*/

    $(".wrap-detail a").click(function(){
        var index=$(this).index();
       /* var pos=$(this).offset().top;*/
        $(".show-c").hide();
        $(this).next().hide().eq(index).slideToggle();
        $("html,body").animate({scrollTop: $(this).offset().top}, 1000);
        /*$("html,body").animate({scrollTop:pos},100);*/
    })


    /*验证提示信息*/
    $(".btn").click(function(){
        $(this).parent().next(".alert-n").find(".font-error").animate(
            {
                top:'-100px',
                opacity:'1',
            }
        ).delay(2000).hide(0);
    })

    /* 进度条加载*/
    function animate(){
        $(".charts").each(function(i,item){
            var a=parseInt($(item).attr("w"));
            $(item).animate({
                width: a+"%"
            },1000);
        });
    }
    animate();
})


