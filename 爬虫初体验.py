#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests


# In[36]:


while True:
    city = input("请输入城市，回车退出：\n")
    if not city:
        break

    req = requests.get(' http://wthrcdn.etouch.cn/weather_mini?city=' + city)

    data = req.json()
    current_weather = data['data']['forecast'][0]
    print(current_weather['date'],current_weather['high'],current_weather['low'],current_weather['type'],sep='\n')


# In[ ]:




