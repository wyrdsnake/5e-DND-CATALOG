from utils import *
import discord
import requests
import random

def list_feats(page=0):
    embed = std_embed()

    res = requests.get('http://www.dnd5eapi.co/api/features')
    if res.status_code != "200": # response 200 == success
        r = dict(res.json())
        feats = [feat['index'] for feat in r['results']]

        ls = ""
        for i in range(50):
            ls += f"{feats[i+(50*page)]}, "
        ls = "None" if ls == "" else ls[:-2]
        embed.add_field(name=f"Feats page {page}", value=ls, inline=False)
    else: 
        embed.add_field(name="error", value="invalid page number?", inline=False)

    return embed

