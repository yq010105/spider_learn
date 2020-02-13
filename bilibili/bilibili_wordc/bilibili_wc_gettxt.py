import requests
import csv
import lxml.html

url = 'https://www.bilibili.com/ranking/'
html = requests.get(url).content.decode()
# print(html)
selector = lxml.html.fromstring(html)
title = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/a/text()')
# print(len(title))
link = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[1]/a/@href')
# print(link[0])
# cover = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[1]/a/div/img/@src')
# print(cover[0])
up_name = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[1]/a/span/text()')
# print(up_name[5])
up_videoplay = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li/div[2]/div[2]/div[1]/span[1]/text()')
time = selector.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[2]/div/span/text()')
time_num = time[0]
str1 = time_num.replace(' 的数据综合得分，每日更新一次','')
str2 = str1.replace('统计所有投稿在 ','')
time_num2 = str2

dir = 'E:/learn/py/git/spider/spider_learn/bilibili/bilibili_wordc/bi' + '.txt'

with open(dir,'w',encoding='gbk') as f:
    for ti in title:
        f.write(ti)
        f.write('\n')

