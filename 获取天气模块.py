#-*-coding：utf-8 -*-
import requests
import json
import os,re

def get():
    str = "长沙"
    url ='http://wthrcdn.etouch.cn/weather_mini?city='+str
    response= requests.get(url)
    wearher_json=json.loads(response.text)
    a=wearher_json['data']
    
    print("{0:-^60}".format("Good Morning"))
    print("当前位置："+a['city'])
    print( "温馨提示："+a['ganmao'])
    print("当前温度："+a['wendu']+'℃')
    print("昨天："+a['yesterday']['date'])
    print("风力："+a['yesterday']['fl'][9:[m.start() for m in re.finditer(']', a['yesterday']['fl'])][0]])
    print("风向："+a['yesterday']['fx'])
    print(a['yesterday']['high'])
    print(a['yesterday']['low'])
    print("天气："+a['yesterday']['type'])
    print("--------------------------------")
    i = 0
    print("今天："+a["forecast"][i]['date'])
    print('风力: '+a["forecast"][i]['fengli'][9:[m.start() for m in re.finditer(']', a['yesterday']['fl'])][0]])
    print('风向：'+a["forecast"][i]['fengxiang'])
    print(a["forecast"][i]['high'])
    print(a["forecast"][i]['low'])
    print("天气："+a["forecast"][i]['type'])
    print("--------------------------------")
    i = 2
    print("明天："+a["forecast"][i]['date'])
    print('风力: '+a["forecast"][i]['fengli'][9:[m.start() for m in re.finditer(']', a['yesterday']['fl'])][0]])
    print('风向：'+a["forecast"][i]['fengxiang'])
    print(a["forecast"][i]['high'])
    print(a["forecast"][i]['low'])
    print("天气："+a["forecast"][i]['type'])
    print("--------------------------------")

get()

        
    
 
