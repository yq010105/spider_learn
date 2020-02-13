import requests
import re
import os
from multiprocessing.dummy import Pool


def get_urls(search_id):
    total = (input('请输入要几页----30张一页----：'))
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + search_id+ '&pn='
    t = 0
    URLS = []
    while t < int(total)*30:
        URL = url + str(t)
        t = t + 30
        URLS.append(URL)
    return URLS

def get_obj(url):
    html = requests.get(url).content.decode()
    obj_URL = re.findall('"objURL":"(.*?)",',html,re.S)
    return obj_URL

def save_pic():
    pool=Pool(5)
    objurls = pool.map(get_obj,URLS)
    i = 1
    for objurl in objurls:
        for obj in objurl:
            print('开始下载图片'+'\t'+'第'+str(i)+'张')
            try :
                pic = requests.get(obj,timeout = 10)
            except requests.exceptions.ConnectionError:
                print('图片无法下载')
                continue
            except requests.exceptions.ReadTimeout:
                print('requests.exceptions.ReadTimeout')
                continue
            global search_id
            main_path = patha +'/' + search_id +'/'
            if not os.path.exists(main_path):
                os.makedirs(main_path)
            dir = main_path + search_id+ str(i) + '.jpg'
            with open(dir,'wb') as f:
                f.write(pic.content)
            i += 1


if __name__ =='__main__':
    search_id = input('请输入要下载的内容:')
    URLS = get_urls(search_id)
    patha = input('输入文件保存路径----示例:E:/baidu----:')
    save_pic()