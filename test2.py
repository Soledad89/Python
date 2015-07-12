#!/usr/bin/python
import requests  #调用urllib2  
url='http://www.baidu.com/s?wd=cloga' #把等号右边的网址赋值给url
html=requests.get(url)   #html随意取名 等号后面的动作是打开源代码页面，并阅读
print(html) #打印
