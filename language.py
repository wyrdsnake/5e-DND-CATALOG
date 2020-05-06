from utils import *
import requests
import discord

# returns a and embed containing info about languages
def language_embed():
    embed = std_embed()
    res = requests.get('http://www.dnd5eapi.co/api/languages')
    if res.status_code != "200": # response 200 == success
        r = dict(res.json())
        indices = [lang['index'] for lang in r['results']]

        for url in indices:
            # waive the response code checking because I'm feeling loose today
            res2 = requests.get(f"http://www.dnd5eapi.co/api/languages/{url}")
            ld = dict(res2.json())

            speakers = ""
            for speaker in ld['typical_speakers']:
                speakers += f"{speaker}, "
            speakers = "None" if speakers == "" else speakers[:-2] 
            payload = f"**Type:** {ld['type']}\n**Speakers:** {speakers}\n**Script:** {ld['script']}"
            embed.add_field(name=f"**{ld['name']}**", value=payload, inline=True)
    
    return embed

