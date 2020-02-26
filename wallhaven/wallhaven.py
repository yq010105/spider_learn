import lxml.html
import requests
import re
import os

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}

def get_url():
    pages = input('输入页数：')
    # pages = '1'
    url_pics = []
    page = 1
    while page <= int(pages):
        url = 'https://wallhaven.cc/search?categories=010&purity=100&resolutions=1280x800&sorting=relevance&order=desc&page=' + str(page)
        html = requests.get(url,headers = headers).content.decode()
    # print(html)
    # exit()
        selector = lxml.html.fromstring(html)

        url_pic = selector.xpath('//*[@id="thumbs"]/section/ul/li/figure/a/@href')
        url_pics.append(url_pic)
        page += 1
    print('得到了内层url')
    return url_pics

def get_pic():
    url_pics = get_url()
    img_urls = []
    for urlst in url_pics:
        for url in urlst:
            htmlp = requests.get(url,headers = headers).content.decode()
            # print(htmlp)
            # exit()
            img_url = re.findall(r'"wallpaper" src="(.*?)"',htmlp,re.S)[0]
            img_urls.append(img_url)
    print('得到图片的url')
    return img_urls

def get_img(imgurl_list):
    i = 1
    for url in imgurl_list:
        print('开始下载图片'+'\t'+'第'+str(i)+'张')
        try:
            pic = requests.get(url, timeout=10)
        except requests.exceptions.ConnectionError:
            print('图片无法下载')
            continue
        except requests.exceptions.ReadTimeout:
            print('requests.exceptions.ReadTimeout')
            continue

        main_path = r'E:\\wallhaven\\' 
        if not os.path.exists(main_path):
            os.makedirs(main_path)

        
        dir = 'E:\\wallhaven\\' + str(i) +'.jpg'

        with open(dir, 'wb') as f:
            f.write(pic.content)
        i += 1

if __name__ == '__main__':
    imgurl_list = get_pic()
    get_img(imgurl_list)