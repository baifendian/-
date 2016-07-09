#coding=utf-8
'''
Created on 2016年6月27日

@author: BFD_487
'''
import urllib2
import json

def download():
    url = "http://waimai.baidu.com/waimai/shoplist/7033186bfbbe1a70?sortby=distance&display=json&page=1&count=40";
    request = urllib2.Request(url);
    request.add_header("Cookie", '''wm_search_addr=[{"name":"%E5%8C%97%E8%BE%B0%E4%B8%96%E7%BA%AA%E4%B8%AD%E5%BF%83A%E5%BA%A7","address":"%E5%8C%97%E8%BE%B0%E8%A5%BF%E8%B7%AF8%E5%8F%B7%E9%99%A22%E5%8F%B7","lat":4839166.18,"lng":12957111.44,"shopnum":1081,"city_id":131}]''');
    response = urllib2.urlopen(request);
    responseJson = response.read();
    pagedata = json.loads(responseJson);
    shopinfo = pagedata["result"]["shop_info"];
    
    shoplist = [];
    for shop in shopinfo:
        shopdata = {};
#         shop_name = shop["shop_name"];
        shopdata["shop_name"] = shop["shop_name"];
        #起送价格
#         takeout_price = shop["takeout_price"];
        shopdata["takeout_price"] = shop["takeout_price"];
        #配送时间
#         delivery_time = shop["delivery_time"];
        shopdata["delivery_time"] = shop["delivery_time"];
        #平均得分
#         average_score = shop["average_score"];
        shopdata["average_score"] = shop["average_score"];
        #月销量
#         saled_month = shop["saled_month"];
        shopdata["saled_month"] = shop["saled_month"];
        #起送价格
#         takeout_cost = shop["takeout_cost"];
        shopdata["takeout_cost"] = shop["takeout_cost"];
        
        welfarelist = [];
        for welfare in shop["welfare_info"]:
            welfarelist.append(welfare["msg"]);
        shopdata["welfare_info"] = welfarelist;
        shoplist.append(shopdata);
    return json.dumps(shoplist)

if __name__ == '__main__':
    file = open("shopinfo.data", 'w')
    file.write(str(download()))