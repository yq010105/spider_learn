import json

js = '{"link":"http://img1.imgtn.bdimg.com/it/u=905665511,4125694826&fm=214&gp=0.jpg"}'
dip = json.loads(js)
print(dip['link'])