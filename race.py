import discord
import requests
import random
from utils import *

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