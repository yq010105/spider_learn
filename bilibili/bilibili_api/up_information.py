import json
import requests


mid = input('输入要查询的up的uid：')
url_space = 'https://api.bilibili.com/x/space/acc/info?mid=' + mid
url_relation = 'https://api.bilibili.com/x/relation/stat?vmid='+mid
space = requests.get(url_space).content.decode()
relation =requests.get(url_relation).content.decode()
# print(type(html))
dict_space = json.loads(space)
dict_rela = json.loads(relation)
# print(dict)
up_name = dict_space["data"]["name"]
up_level = dict_space['data']['level']

up_following_num = dict_rela['data']['following']
up_follower_num = dict_rela['data']['follower']

print(f'up名字是:{up_name}')
print(f'up等级达到:{up_level}级')
if int(up_level)>=5:
    print('----哇是个大佬！！！----')
print(f'up关注了{up_following_num}个人')
if int(up_following_num)>=700: 
    print('----铁定是个dd！！！----')
print(f'up有{up_follower_num}个粉丝')
