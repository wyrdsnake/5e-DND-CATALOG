import requests
import json 

url = "http://www.dnd5eapi.co/api/"
base = "http://www.dnd5eapi.co"

with open("./index/proficiencies.json", "r") as f:
    d = dict(json.load(f))
    for res in d['results']:
        print(res['url'])
        with open(f"./index/proficiencies/{res['index']}.json", "w") as f2:
            res2 = (requests.get(f"{base}{res['url']}"))
            json.dump(res2.json(), fp=f2, indent=4)



# with open("./index/ability-scores.json", "w") as index:
#     # json.dump(res.json(), fp=index, indent=4)
#     print("Gathering index...")

# d = dict(res.json())

# for key in d.keys():
#     with open(f"./index/{key}.json", "w") as f:
#         res2 = (requests.get(f"{base}{d[key]}"))
#         json.dump(res2.json(), fp=f, indent=4)
#         print(d[key])





