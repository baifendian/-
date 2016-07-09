#coding=utf-8
'''
Created on 2016年6月27日

@author: BFD_487
'''
import urllib
import urllib2

# use cookie
'''
Cookie:w_cid=110100; w_cpy_cn="%E5%8C%97%E4%BA%AC"; w_cpy=beijing; waddrname="%E5%8C%97%E8%BE%B0%E4%B8%96%E7%BA%AA%E4%B8%AD%E5%BF%83A%E5%BA%A7"; w_geoid=wx4g8dgz50m6; w_ah="40.00654388219118,116.39444578438997,%E5%8C%97%E8%BE%B0%E4%B8%96%E7%BA%AA%E4%B8%AD%E5%BF%83A%E5%BA%A7"
Uer-Agent:User-Agent:Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1
'''

def download():
#     value = {"classify_type":"cate_all","sort_type":"3","price_type":"0","support_online_pay":"0","support_invoice":"0","support_logistic":"0","page_offset":"1","page_size":"20"};
#     valuedata = urllib.urlencode(value);
    url = "http://waimai.meituan.com/home/wx4g8dgz50m6";
    request = urllib2.Request(url);
    request.add_header("Cookie", '''w_cid=110100; w_cpy_cn="%E5%8C%97%E4%BA%AC"; w_cpy=beijing; waddrname="%E5%8C%97%E8%BE%B0%E4%B8%96%E7%BA%AA%E4%B8%AD%E5%BF%83A%E5%BA%A7"; w_geoid=wx4g8dgz50m6; w_ah="40.00654388219118,116.39444578438997,%E5%8C%97%E8%BE%B0%E4%B8%96%E7%BA%AA%E4%B8%AD%E5%BF%83A%E5%BA%A7"''');
    request.add_header("User-Agent", "User-Agent:Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1");
    response = urllib2.urlopen(request);
    html = response.read();
    print "html is:%s" % html

if __name__ == '__main__':
    download()