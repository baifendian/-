#coding=utf-8
'''
Created on 2016年7月8日

@author: BFD_487
'''
import urllib2
import time
import json

basicurl = "http://feed.mix.sina.com.cn/api/roll/get?pageid=1&lid=21&num=10&ctime=%s&encode=utf-8&callback=feedCardJsonpCallback"

def downloadNews():
    news = []
    timestr = str(time.time()).split(".")[0]
    response = urllib2.urlopen(basicurl % timestr)
    responseJson = response.read()
    beginIndex = responseJson.index("(")+1
    endIndex = responseJson.rfind(")")-10
    jsonObj = json.loads(responseJson[beginIndex : endIndex])
    datalist = jsonObj["result"]["data"]
    for data in datalist:
        new = {}
        new["title"] = data["title"]
        new["time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(data["intime"])))
        new["summary"] = data["summary"]
        news.append(new)
    return json.dumps(news)
if __name__ == '__main__':
#     print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1467985753))
    file = open("index.data", "a")
    file.write(str(downloadNews()))