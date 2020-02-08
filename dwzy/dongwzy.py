import requests
import re
from multiprocessing.dummy import Pool

url = 'https://www.kanunu8.com/book3/6879'
headers = {
    "UserAgent" :
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 Edg/80.0.361.48"
}
# fd = open('nongc.txt','a')
response = requests.get(url ,headers=headers)
response.encoding = 'GBK'
html = response.text
# print(html)
htmlst = []
title_name_lst = []
def get_htmlst():
    dl = re.findall(r'<table cellspacing="1" cellpadding="8" width="800" align="center" bgcolor="#d4d0c8" border="0">.*?</table>',html,re.S)
    for i in dl :
        dl1 = re.findall(r'href="(.*?)">(.*?)</a>',i)
        x = 0
        while x < len(dl1) :
            dl2 = dl1[x]
            x += 1
            html1 = "https://www.kanunu8.com/book3/6879/" + dl2[0]
            title_name = dl2[1]
            htmlst.append(html1)
            title_name_lst.append(title_name)
            # fd.write(title_name)
            # fd.write(html)
            # print(title_name,end= "\t")
            # print(html1)

def get_content(self):
    link = requests.get(self,headers = headers)
    if True :
        link.encoding = 'GBK'
        yuanma = link.text
        html1 = re.findall(r'<p>.*?</p>',yuanma,re.S)[0]
        html2 = html1.replace('<br>','\n')
        html3 = html2.replace('"',' ')
        html4 = html3.replace('<br />',' ')
        html5 = html4.replace('<p>',' ')
        html6 = html5.replace('</p>',' ')
    return html6
# print(htmlst)    #['https://www.kanunu8.com/book3/6879/131779.html', 'https://www.kanunu8.com/book3/6879/131780.html', 'https://www.kanunu8.com/book3/6879/131781.html', 'https://www.kanunu8.com/book3/6879/131782.html', 'https://www.kanunu8.com/book3/6879/131783.html', 'https://www.kanunu8.com/book3/6879/131784.html', 'https://www.kanunu8.com/book3/6879/131785.html', 'https://www.kanunu8.com/book3/6879/131786.html', 'https://www.kanunu8.com/book3/6879/131787.html', 'https://www.kanunu8.com/book3/6879/131788.html']['https://www.kanunu8.com/book3/6879/131779.html', 'https://www.kanunu8.com/book3/6879/131780.html', 'https://www.kanunu8.com/book3/6879/131781.html', 'https://www.kanunu8.com/book3/6879/131782.html', 'https://www.kanunu8.com/book3/6879/131783.html', 'https://www.kanunu8.com/book3/6879/131784.html', 'https://www.kanunu8.com/book3/6879/131785.html', 'https://www.kanunu8.com/book3/6879/131786.html', 'https://www.kanunu8.com/book3/6879/131787.html', 'https://www.kanunu8.com/book3/6879/131788.html']
# print(title_name_lst)    #['第一章', '第二章', '第三章', '第四章', '第五章', '第六章', '第七章', '第八章', '第九章', '第十章']

# print(result)       #['content','']
def write_con():
    for j in range(10):
        fd = open(f'{title_name_lst[j]}.txt','w',encoding='GBK')
        fd.write(title_name_lst[j])
        fd.write('\n')
        fd.write(result[j])
        fd.close()

get_htmlst()
pool = Pool(3)
result = pool.map(get_content,htmlst)
write_con()
