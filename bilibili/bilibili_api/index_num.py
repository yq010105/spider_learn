import requests
import json
import time

def print_num():
    index = requests.get(
    'https://api.bilibili.com/x/web-interface/online?&;jsonp=jsonp').content.decode()
    dict_index = json.loads(index)
    all_count = dict_index['data']['all_count']
    web_online = dict_index['data']['web_online']
    play_online = dict_index['data']['play_online']
# 应该是人数和实时在线人数
    print(f'all_count:{all_count}')
    print(f'web_online:{web_online}')
    print(f'play_online:{play_online}')


for i in range(100):
    print(f'第{i+1}次计数')
    print_num()
    time.sleep(2)
