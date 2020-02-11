import requests
import json
import lxml.html
import re
import os

# 获取src
def get_src():
    url = 'https://www.instagram.com/baaaakuuuu'
    html = requests.get(url).content.decode()
    selector = lxml.html.fromstring(html)
    script = selector.xpath('/html/body/script[1]/text()')[0].strip()
    # print(script)
    # print(type(script))       #str
    # exit()
    # for script_in in script :
        # try:
        #     script_dic = json.loads(script_in)
        # print(script_dic)
    src = re.findall(r'"thumbnail_resources":\[(.*?)\]',script,re.S)
    # print(src[0]) #str
    # print(type(src[0]))
    # exit()
    return src

# 获取图片链接
def get_picurl():
    src = get_src()
    # print(src)
    # exit()
    pic_url_lst = []
    for src_ls in src :         #"config_height":480},{ ... ,"config_width":640,"config_height":640}
        thumb = re.findall(r'"config_height":480},{(.*?),"config_width":640,"config_height":640}',src_ls)[0]
        thumb_json = '{' + thumb + '}'
        # print(thumb_json)
        # exit()
        thumb_py = json.loads(thumb_json)
        pic_url = thumb_py['src']
        # print(pic_url)
        # exit()
        pic_url_lst.append(pic_url)
    # print(pic_url_lst)
    # exit()
    return pic_url_lst


# 将图片链接保存
def save_pic():
    pic_url_lst = get_picurl()
    i = 1
    # print(pic_url_lst)
    # exit()
    for pic_con in pic_url_lst:
        # print(pic_con)
        # exit()
        try:
            pic = requests.get(pic_con, timeout=10)
            main_path = 'E:/ins/'
            if not os.path.exists(main_path):
                os.makedirs(main_path)
            path = 'E:/ins/' + 'baku' + str(i) + '.jpg' 
            with open(path,'wb') as f:
                f.write(pic.content)
                print(f'第{i}张已下载')
            i +=1
        except requests.exceptions.ConnectionError:        #requests.exceptions.ConnectionError
            print('图片无法下载')
            continue
    return 

save_pic()