import requests
import re
import os


def get_id(search_id):
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=' + search_id
    return url


def get_obj():
    url = get_id(search_id)
    html = requests.get(url).content.decode()
    obj_URL = re.findall('"objURL":"(.*?)",', html, re.S)
    return obj_URL


def save_pic():
    obj_url = get_obj()
    i = 1
    for objurl in obj_url:
        print('开始下载图片'+'\t'+'第'+str(i)+'张')
        try:
            pic = requests.get(objurl, timeout=10)
        except requests.exceptions.ConnectionError:
            print('图片无法下载')
            continue
        except requests.exceptions.ReadTimeout:
            print('requests.exceptions.ReadTimeout')
            continue
        global search_id
        main_path = r'E:\learn\py\git\spider\spider_learn\baidu\pic\\' + search_id + '\\'
        if not os.path.exists(main_path):
            os.makedirs(main_path)
        dir = "E:\learn\py\git\spider\spider_learn\\baidu\pic\\" + \
            search_id + '\\' + search_id + str(i) + '.jpg'
        with open(dir, 'wb') as f:
            f.write(pic.content)
        i += 1


if __name__ == '__main__':
    search_id = input('请输入要下载的内容:')
    save_pic()

    # search_id = input('请输入要下载的内容:')
    # url = get_id(search_id)
    # print(url)
    # obj_url = get_obj()
    # # print(type(obj_url))
    # print(obj_url)
