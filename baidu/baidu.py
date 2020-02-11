# 网上找的一篇

import re
import requests
import os 

def download(html):
    #通过正则匹配
    pic_url = re.findall('"thumbURL":"(.*?)",',html, re.S)
    i = 1
    for key in pic_url:
        print("开始下载图片："+key +"\r\n")
        try:
            pic = requests.get(key, timeout=10)
        except requests.exceptions.ConnectionError:
            print('图片无法下载')
            continue
        #保存图片路径             
        main_path="E:/baidu/" #文件保存路径，如果不存在就会被重建
        if  not os.path.exists(main_path):#如果路径不存在
            os.makedirs(main_path)
        dir = "E:/baidu/" + str(i) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
def main():
        url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=result&pos=history&word=siyueshinide'
        result = requests.get(url)
        download(result.text)
 
 
if __name__ == '__main__':
        main()