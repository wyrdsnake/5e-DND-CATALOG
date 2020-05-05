from utils import *
import requests
import discord

# returns a and embed containing info about languages
def ability_embed(ab=None):
    embed = std_embed()
    if ab is None:    ## display list of langs
        res = requests.get('http://www.dnd5eapi.co/api/ability-scores')
        if res.status_code != "200": # response 200 == success
            r = dict(res.json())
            names = [score['name'] for score in r['results']]

            for name in names:
                # waive the response code checking because I'm feeling loose today
                res2 = requests.get(f"http://www.dnd5eapi.co/api/ability-scores/{name.lower()}")
                r2 = dict(res2.json())
                breif = r2['desc'][0]
                embed.add_field(name=f"{name}", value=breif, inline=False)
        else: 
            embed.add_field(name="error", value="¯\_(ツ)_/¯ ")
        
        embed.add_field(name="Help", value="Type `?dnd abilities <ability>` for more info about a specific ability score", inline=False)
    else: 
        res = requests.get(f"http://www.dnd5eapi.co/api/ability-scores/{ab.lower()}")
        r = dict(res.json())
        embed.description = generate_lore(f"{r['full_name']} ability")

        description = ""
        for desc in r['desc']:
            description += f"{desc}\n"
        description = "None" if description == "" else description[:-2]
        embed.add_field(name=f"{r['full_name']} ({r['name']})", value=description, inline=False)

        skills = ""
        for skill in r['skills']:
            skills += f"{skill['name']}, "
        skills = "None" if skills == "" else skills[:-2]

        embed.add_field(name="Skills", value=skills, inline=False)

    return embed
  
