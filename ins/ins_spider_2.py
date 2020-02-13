import requests
import lxml.html
import re

class INS(object):
    
    ins_url= ''

    headers = {
        ':authority': 'www.instagram.com',
        ':method': 'GET',
        ':path': '/baaaakuuuu/',
        ':scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': 'ig_did=675BE67D-DEA9-4992-8671-A02744F10E87; mid=XkKyLQALAAEPnD104erm6Rb42y1z; csrftoken=sMUHAYgqfKJ5Wr4lad9c5bflY4hj5egm; shbid=2232; shbts=1581429384.1046433; ds_user_id=16113660604; sessionid=16113660604%3AqrEfICAmSUw06N%3A11; rur=FTW; urlgen="{\"203.218.243.50\": 4760}:1j1jem:PwwuZkZpufAx9U8Mj_GKz7WbPb8"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    }
    def __init__(self,url):
        self.url = url
        self.get_links()

        # get_pic()

    def get_source(self,url,headers):
        return requests.get(url,headers).content.decode()
    
    def get_links(self):
        source =self.get_source(self.url,self.headers)
        selector = lxml.html.fromstring(source)
        script = selector.xpath('/html/body/script[1]/text()')[0].strip()
        print(script)
        exit()
        links = re.findall(r'"shortcode":"(.*?)"',script,re.S)
        print(links[0])

        return links

if __name__ == "__main__":
    spider = INS('https://www.instagram.com/baaaakuuuuu/')

