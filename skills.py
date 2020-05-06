from utils import *
import requests
import discord

# returns a and embed containing info about languages
def skills_embed(skill=None):
    embed = std_embed()
    if skill is None:    ## display list of langs
        res = requests.get('http://www.dnd5eapi.co/api/skills')
        if res.status_code != "200": # response 200 == success
            r = dict(res.json())
            skills = [skill['index'] for skill in r['results']]

            for skill in skills:
                res2 = requests.get(f"http://www.dnd5eapi.co/api/skills/{skill}")
                r2 = dict(res2.json())

                embed.add_field(name=r2['name'], value=r2['ability_score']['name'], inline=True)
        else: 
            embed.add_field(name="error", value="Make sure the skill specified is supported", inline=False)
        
        embed.add_field(name="Help", value="Type `?dnd skills <skill>` for more info about a specific skill", inline=False)
    else: 
        res = requests.get(f"http://www.dnd5eapi.co/api/skills/{skill.lower()}")
        if res.status_code != "200": # response 200 == success 
            r = dict(res.json())
            embed.description = generate_lore(f"{['name']} skill")

            description = ""
            for desc in r['desc']:
                description += f"{desc}\n "
            description = "None" if description == "" else description[:-2]
            
            embed.add_field(name=f"**{r['name']}:** {r['ability_score']['name']}", value=description, inline=False)
        else: 
            embed.add_field(name="error", value="Make sure the skill specified is supported", inline=False)


    return embed
  
