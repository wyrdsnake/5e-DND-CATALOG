# This file should hold all the logic so that bot.py is easy to read

import discord
import requests
import random

# creates a standard message
def std_embed():
    embed=discord.Embed(title="**Calligula's Compendium**", color=0xEA4246, description="A bot that compiles races, classes, equipment, and more!")
    return embed

# Appends the standard footer to a given message and return the new embed
def std_footer(embed):
    embed.add_field(name="Links", value="[Support Calligula](https://www.google.com) | [5e API](https://https://www.dnd5eapi.co/) | [Invite]({})".format("google.com","google.com" ) , inline=False)
    

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

