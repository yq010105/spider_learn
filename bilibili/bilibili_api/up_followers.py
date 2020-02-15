import requests
import json
import csv
import os
import time

uid = input('请输入查找的up主的uid:')
url = 'https://api.bilibili.com/x/relation/followers?vmid=' + \
    uid + '&ps=0&order=desc&jsonp=jsonp'

html = requests.get(url).content.decode()
dic_html = json.loads(html)

index_order = dic_html['data']['list']
mids, mtimes, unames, signs = [], [], [], []
for i in index_order:
    mid = i['mid']
    mids.append(mid)
    mtime = i['mtime']
    mmtime = time.asctime(time.localtime(mtime))
    mtimes.append(mmtime)
    uname = i['uname']
    unames.append(uname)
    sign = i['sign']
    signs.append(sign)
# print(index_order)
# print(mids)
headers = ['uid', '注册时间', 'up姓名', '个性签名']
rows = []
j = 0
for j in range(len(mids)):
    rows.append([mids[j], mtimes[j], unames[j], signs[j]])

main_path = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\csv'
if not os.path.exists(main_path):
    os.makedirs(main_path)

dir = 'E:\\learn\\py\\git\\spider\\spider_learn\\bilibili\\bilibili_api\\csv\\' + \
    'follers' + '.csv'

with open(dir, 'w', encoding='utf-8') as f:
    fb = csv.writer(f)
    fb.writerow(headers)
    fb.writerows(rows)


print('----最多只显示一页的粉丝数，也就是50个----')
print(f'共有{len(mids)}个粉丝')
