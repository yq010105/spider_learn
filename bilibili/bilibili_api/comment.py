import json
import requests
from multiprocessing.dummy import Pool
import re
import os
import time

av = input('请输入视频的av号:')
p_total = input('请输入评论要几页:')


def get_urls():
    urls = []
    p = 1
    while p <= int(p_total):
        url = 'http://api.bilibili.com/x/v2/reply?jsonp=jsonp&;pn=' + \
            str(p) + '&type=1&oid=' + av
        urls.append(url)
        p += 1
    return urls


def get_name_con(url):
    html = requests.get(url).content.decode()
    yh_names = re.findall(r'"uname":"(.*?)","sex":', html, re.S)
    yh_contents = re.findall(r'"message":"(.*?)","plat"', html, re.S)
    del yh_contents[0]
    yh_contents2 = []
    for yh_content in yh_contents:
        yh_contents2.append(yh_content.replace('\\n', ' '))
    # print(yh_contents2)
    # exit()
    return yh_names, yh_contents2


def get_names_cons():
    pool = Pool(5)
    urls = get_urls()
    namecons = pool.map(get_name_con, urls)
    names = []
    cons = []
    for namecon in namecons:
        name = namecon[0]
        for n in name:
            names.append(n)
        con = namecon[1]
        for c in con:
            cons.append(c)
    return names, cons


def save():
    tumple = get_names_cons()
    namelst = tumple[0]
    conlst = tumple[1]
    # print(len(conlst))
    # # print(type(namelst))
    # print(len(namelst))
    # exit()
    if len(namelst) != len(conlst):
        tot = len(conlst)
    g = 0
    main_path = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\txt'  # 修改路径-自定义
    if not os.path.exists(main_path):
        os.makedirs(main_path)

    dir1 = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\txt\\' + \
        'comment' + '.txt'  # 自定义文件名
    with open(dir1, 'w', encoding='utf-8') as fb:
        for g in range(tot):
            # fb.write(namelst[g])
            # fb.write('\t\t\t')
            fb.write(conlst[g])
            # fb.write('\n')
            g += 1


if __name__ == '__main__':
    start = time.time()
    print(time.asctime(time.localtime(start)))
    save()
    end = time.time()
    print(time.asctime(time.localtime(end)))
    print(f'----已完成----用了{end - start}s时间', end='\t')
    print(f'此视频已获得 {p_total} 页的评论')
