# This file should hold all the logic so that bot.py is easy to read

import discord
import requests
import random

# creates a standard message
def std_embed():
    embed=discord.Embed(title="**Calligula's Compendium**", color=0xEA4246, description="A bot that compiles races, classes, equipment, and more!")
    return embed

# used for specific race info
def race_embed(_race):
    embed = std_embed()
    res = requests.get(f'http://www.dnd5eapi.co/api/races/{_race.lower()}')
    if res.status_code != "200": # response 200 == success
        r = dict(res.json())
        result = { 
            "name": r['name'],
            "speed": r['speed'],
            "ability-bonuses": [f"{bonus['name']}: {bonus['bonus']}"  for bonus in r['ability_bonuses'] ],
            "age": r['age'],
            "age": r['alignment'],
            "size": f"{r['size_description']}",
            "language": r['language_desc'],
            "traits": [f"{trait['name']}" for trait in r['traits']],
            "subraces": [f"{sub['name']}" for sub in r['subraces']]
            }

        embed.description = generate_lore(f"{result['name']} race")
        embed.add_field(name="Name", value=result['name'], inline=True)
        embed.add_field(name="Speed", value=f"{result['speed']} ft/s", inline=True)
        
        ls = ""
        for sr in result['subraces']:
            ls += f"{sr}, "
        ls = "None" if ls == "" else ls[:-2]
        embed.add_field(name="Subraces", value=ls, inline=True)
        
        embed.add_field(name="Age", value=result['age'], inline=False)
        embed.add_field(name="Size", value=result['size'], inline=False)
        embed.add_field(name="Language", value=result['language'], inline=False)

        ls = ""
        for trait in result['traits']:
            ls += f"{trait}, "
        ls = "None" if ls == "" else ls[:-2]
        embed.add_field(name="Traits", value=ls, inline=True)
        
        ls = ""
        for ab in result['ability-bonuses']:
            ls += f"{ab}, "
        ls = "None" if ls == "" else ls[:-2]
        embed.add_field(name="Ability Bonuses", value=ls, inline=True)

    else: 
        embed.add_field(name="error", value="Make sure the race specified is supported", inline=False)

    return embed

# used for specific race info
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

        embed.description = generate_lore(f"{result['name']} class")
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
            embed.add_field(name="Description", value=result['desc'], inline=False)

            ls = ""
            for feat in result['feats']:
                ls += f"{feat} -- `?dnd feat {feat.replace(' ', '-').lower()}` for more info,\n"
            ls = "None" if ls == "" else ls[:-2]
            embed.add_field(name="Feats", value=ls, inline=False)


        else:
            embed.add_field(name="error", value="Make sure the class specified is supported", inline=False)
 
    else: 
        embed.add_field(name="error", value="Make sure the class specified is supported", inline=False)

    return embed


# generates some lore about the given request
def generate_lore(item):
    options = [
        f"_Ah, yes, the {item}..._",
        f"_A wandering traveler once asked me about {item}..._",
        f"_Look at that, the {item}..._ is detailed on page 1!_",
        f"_How drab. If you must know about {item} here it is._",
        f"_How do you not know about the {item} yet? Even mud golems knows about the {item}_",
        f"_I don't think I've read about {item}... Just kidding of course_",
        f"_In my opinion, knowledge of {item} should be restricted..._" 
    ]
    return random.choice(options)

