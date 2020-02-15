import requests
import re
import os
import json

def get_pic():
    if fenqu == '':
        fenqu1 = 'shuma'
    else :
        fenqu1 = fenqu 

    html = requests.get(
        'https://www.bilibili.com/index/ding.json').content.decode()

    dict_html = json.loads(html)
    i = 0
    aids = []
    pics = []

    for i in range(10):
        aid = dict_html[fenqu][str(i)]['aid']
        pic = dict_html[fenqu][str(i)]['pic']
        aids.append(aid)
        pics.append(pic)

    j = 1
    h = j-1
    for h in range(10):
        main_path = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\pic\\'+fenqu1
        if not os.path.exists(main_path):
            os.makedirs(main_path)
        try:
            piccc = requests.get(pics[h])
        except requests.exceptions.ConnectionError:
            print('图片无法下载')
            continue
        except requests.exceptions.ReadTimeout:
            print('requests.exceptions.ReadTimeout')
            continue
        dir = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\pic\\' + \
            fenqu1 + '\\'  +'av' + str(aids[h]) + '.jpg'
        with open(dir, 'wb') as f:
            print(f'正在爬取第{j}张图')
            f.write(piccc.content)
        j += 1
        h += 1

to = int(input('请输入你要爬多少次---一次最多十张：'))
print('-douga-teleplay-kichiku-dance-bangumi-fashion-life-ad-guochuang-movie-music-technology-game-ent--')
fenqu = input('请输入爬取分区:')
for i in range(to):
    get_pic()
    print(f'----完成第{i+1}次图片爬取----')
