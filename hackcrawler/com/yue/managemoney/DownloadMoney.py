#coding=utf-8
'''
Created on 2016年7月9日

@author: BFD_487
'''
import urllib2
import json

url = "http://www.cmbchina.com/cfweb/svrajax/product.ashx?op=search&type=m&pageindex=2&salestatus=&baoben=&currency=&term=&keyword=&series=01&risk=&city=&date=&pagesize=10&orderby=ord1"

def downloadmoney():
    file = open("managemoneylist.data", 'w')
    response = urllib2.urlopen(url)
    result = response.read()
    length = len(result)
    beginIndex = result.index("[")
    list = result[beginIndex:length-2]
    list = list.replace("{", "{\"").replace(":\"", "\":\"").replace("\",", "\",\"")
    file.write(list)

downloadmoney()
