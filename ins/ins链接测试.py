import json
# import requests

json_t = '{"3":"\u30a2\u30d7\u30ea\u3092\u5229\u7528"}'
# html_json = requests.get('').content.decode()
# html_dict = {'url':'p/B8ViujtleSp/'}
# html_json = json.dumps(html_dict)
html_dict = json.loads(json_t)
print(html_dict)

# print(html_json)
# print(type(html_json))
# '''
# dic_json = json.loads(json_t)
# print(type(json_t))
# print(type(dic_json))
# print(dic_json['src'])
# '''

# import requests
# import re
# import lxml.html
# import json
# url = 'https://www.instagram.com/baaaakuuuuu/'
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'

# }
# html = requests.get(url,headers=headers).content.decode()
# selector = lxml.html.fromstring(html)
# script = selector.xpath('/html/body/script[1]/text()')[0].strip()
# print(script)
# half_links = re.findall(r'"shortcode":"(.*?)"',html,re.S)
# # print(type(script))
# # print(half_dic)

# # 初始化selenium
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# import time

# driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
# driver.get('https://www.instagram.com/baaaakuuuu/')

# time.sleep(5)
# try :
#     WebDriverWait(driver,30).until(EC.text_to_be_present_in_element(By.CLASS_NAME,"content"),'通关')
# except Exception as _:
#     print('网页加载太慢，爬')

# element = driver.find_element_by_xpath('//div[@class="content"]')
# print(f'异步加载的内容是：{element.text}')

# driver.quit()
# #//*[@id="react-root"]/section/main/div/div[4]/article[1]/div/div/div[1]/div[1]/a