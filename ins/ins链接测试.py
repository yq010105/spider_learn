import json

json_t = '{"src":"https://instagram.fhkg3-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/c0.180.1440.1440a/s640x640/83779595_192353848582583_73956261340772319_n.jpg?_nc_ht=instagram.fhkg3-2.fna.fbcdn.net\\u0026_nc_cat=111\\u0026_nc_ohc=GNq_V7lMz68AX83o-xL\\u0026oh=2181260838a0db2e4d2fb569996b8d1c\\u0026oe=5ED7DA7B"}'
dic_json = json.loads(json_t)
print(type(json_t))
print(type(dic_json))
print(dic_json['src'])
