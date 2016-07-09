#coding=utf-8
'''
Created on 2016年7月9日

@author: BFD_487
'''

import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/heweather/weather/free?city=beijing'


req = urllib2.Request(url)

req.add_header("apikey", "1afc06ac6abec2eb3a95884f7c7ee8f0")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    file = open("weather.data", "w")
    print(content)
    file.write(content)