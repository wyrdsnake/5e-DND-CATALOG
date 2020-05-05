from utils import *
import discord
import requests
import random

# used for specific class info
def class_embed(_class):
    embed = std_embed()

    res = requests.get(f'http://www.dnd5eapi.co/api/classes/{_class.lower()}')
    if res.status_code != "200": # response 200 == success
        r = dict(res.json())
        result = { 
            "name": r['name'],
            "hit_die": r['hit_die'],
            "prof_choices": [ f"{prof['name']}" for prof in r['proficiency_choices'][0]['from'] ],
            "profs": [ f"{prof['name']}" for prof in r['proficiencies'] ],
            "throws": [ f"{throw['name']}" for throw in r['saving_throws'] ],
            "subclasses": [ f"{sub['name']}" for sub in r['subclasses']]
            }

        embed.description = generate_lore(f"the {result['name']} class")
        embed.add_field(name="Name", value=result['name'], inline=True)
        embed.add_field(name="Hit Die", value=f"{result['hit_die']}", inline=True)

        ls = ""
        for throws in result['throws']:
            ls += f"{throws}, "
        ls = "None" if ls == "" else ls[:-2]
        embed.add_field(name="Throws", value=ls, inline=True)

        ls = ""
        for prof in result['profs']:
            ls += f"{prof}, "
        ls = "None" if ls == "" else ls[:-2]
        embed.add_field(name="Proficiencies", value=ls, inline=False)

        ls = ""
        for pc in result['prof_choices']:
            ls += f"{pc[6:]}, "
        ls = "None" if ls == "" else ls[:-2]
        embed.add_field(name="Proficiency Choices", value=ls, inline=False)

        ls = ""
        for sc in result['subclasses']:
            ls += f"{sc} -- `?dnd class {result['name'].lower()} subclass {sc.lower()}` for more info,\n"
        ls = "None" if ls == "" else ls[:-2]
        embed.add_field(name="Subclasses", value=ls, inline=False)
        embed.add_field(name="Levels", value=f"Type `?dnd class {result['name'].lower()} levels` for information about {result['name'].lower()} levels", inline=False)
    else: 
        embed.add_field(name="error", value="Make sure the class specified is supported", inline=False)

    return embed

# returns a list of subclasses for the given _class
def subclass_embed(_class):
    res = requests.get(f'http://www.dnd5eapi.co/api/classes/{_class.lower()}/subclasses')
    embed = std_embed()
    if res.status_code != "200": # response 200 == success
        r = dict(res.json())
        subclass = r['results'][0]['index']
        res = requests.get(f'http://www.dnd5eapi.co/api/subclasses/{subclass}')
        if res.status_code != "200": # response 200 == success
            r = dict(res.json())
            result = {
                "title": f"{r['class']['name']}: {r['name']}",
                "flavor": f"{r['subclass_flavor']}",
                "desc": f"{r['desc'][0]}",
                "feats": [f"{feat['name']}" for feat in r['features'] ]
            }
            embed.add_field(name=result['title'], value=result['flavor'], inline=False)
            
            if len(result['desc']) >= 1024: # some descriptions are too long
                embed.add_field(name="Description", value=result['desc'][:1010]+ "...", inline=False)
                print(len(result['desc'][:1010].join("...")))
            else: 
                embed.add_field(name="Description", value=result['desc'], inline=False)
            print(result)

            ls = ""
            for feat in result['feats']:
                ls += f"{feat} -- `?dnd feat {feat.replace(' ', '-').lower()}` for more info,\n"
            ls = "None" if ls == "" else ls[:-2]
            embed.add_field(name="Feats", value=ls, inline=False)
            # also fetch from other db here

        else:
            embed.add_field(name="error", value="Make sure the class specified is supported", inline=False)
 
    else: 
        embed.add_field(name="error", value="Make sure the class specified is supported", inline=False)

    return embed
