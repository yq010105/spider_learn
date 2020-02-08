import requests
import re
import csv
# import time
#
# """格式化成2016-03-20 11:45:39形式"""
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

url = 'https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3'
headers = {
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}

response = requests.get(url ,headers = headers)
response.encoding = 'utf-8'
html = response.text

title = re.findall(r'统计.*?一次',html)[0]
# print(title)
# exit()
fb = open('bilibili.txt','a',encoding='utf-8')
# print(html)<ul class="rank-list">
fb.write(title)
fb.write('\n')
dl = re.findall(r'<ul class="rank-list">.*?</ul>',html,re.S)[0]
# print(dl)
dl2 = re.findall(r'<div class="info">.*?</div>',dl)
# print(dl2)
# dl3 = re.search(r'href="(.*?)" target="_blank" class="title">(.*?)<',dl2)
# print(dl3)
i = 0
for lt in dl2 :
    lst1 = re.findall(r'href="(.*?)" target="_blank" class="title">(.*?)<',lt)
    # print(lst1)
    # exit()
    i += 1
    for lt1 in lst1:
        lt1_url,lt1_title =lt1
        fb.write(f'第{i}名')
        fb.write('\t')
        fb.write(lt1_url)
        fb.write('\t \t')
        fb.write(lt1_title)
        fb.write('\n')


fb.write('\n\n')
fb.close()

