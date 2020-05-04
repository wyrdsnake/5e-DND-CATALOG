import requests
import json

url = 'http://www.dnd5eapi.co/api/proficiencies/'
res = requests.get(url)
res_json = res.json()
print(list(res_json))

d = dict(res_json)

# print(d['results'])
names = []
for n in d['results']:
    names.append(n['index'])

print(names)