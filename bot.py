# bot.py

import discord
from discord.ext import commands, tasks
import requests
from conf import *
from utils import *
from _class import * 
from race import *
from feat import *

client = commands.Bot(command_prefix = '?dnd ') # set our prefix acc. to guild.id 
client.remove_command('help')                   # Remove the default help command

## debug methods
@client.event
async def on_ready():
    change_status.start() # starts the change_presence cron task
    print('Time to roll.')


@client.event 
async def on_member_join(member):
    print(f'{member} has joined a server. ')


@client.event
async def on_memeber_remove(member):
    print(f'{member} has left a server')


## client commands ##

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! ping = {round(client.latency *1000)} ms')

# Sets a cron to change bot status every 5 minutes 
@tasks.loop(minutes=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(STATUSES)))

# Displays information about supported races
@client.command(aliases=["r", "races"])
async def race(ctx, race=None):

    if race is None:
        embed = std_embed()
        res = requests.get('http://www.dnd5eapi.co/api/races/')
        d = dict(res.json())

        races = []
        ls = ""
        for n in d['results']:
            races.append(n['name'])
            ls += f"{n['name']}, "
        ls =ls[:-2] 
        embed.add_field(name="Supported Races", value=ls, inline=False)
    else: 
        embed = race_embed(race)
    
    std_footer(embed)
    await ctx.send(embed=embed)

 # here we use _class since 'class' is a reserved keyword in python and just add 'class' as an alias
@client.command(aliases=["c", "classes", "class"])
async def _class(ctx, *args): 
    embed = std_embed()
    if len(args) == 0:
        res = requests.get('http://www.dnd5eapi.co/api/classes/')
        d = dict(res.json())

        classes = []
        ls = ""
        for n in d['results']:
            classes.append(n['name'])
            ls += f"{n['name']}, "
        ls =ls[:-2] 
        embed.add_field(name="Supported Classes", value=ls, inline=False)
    elif len(args) == 1: # ?dnd class args[0]
        embed = class_embed(args[0])
    elif len(args) == 2 and (args[1] == "sc" or args[1] == "sub" or args[1] == "subclass" or args[1] == "subclasses"): # asking about subclasses
        embed = subclass_embed(args[0]) # ?dnd class <class> args[1] 

    std_footer(embed)
    await ctx.send(embed=embed)

@client.command(aliases=['feature', 'f', 'features'])
async def feat(ctx, *args):
    embed = std_embed()
    page = 0

    if len(args) == 0: # list page 1 of feats
        embed = list_feats()
    elif args[0].isdigit(): # list page n of feats
        page = args[0] 
        embed = list_feats(page)
    else:       # display specific feat
        pass

    std_footer(embed)
    await ctx.send(embed=embed)






# Displays information about the bot
@client.command(aliases=['i'])
async def info(ctx):
    embed = std_embed()
    embed.add_field(name="Written", value="@wyrdsnake\n@MurphyPone\n@Kabir")
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")
    embed.add_field(name="Invite", value="TODO")
    std_footer(embed)
    await ctx.send(embed=embed)


# Displays the help message for the bot 
@client.command(name="help", aliases=['h'])
async def help(ctx, *args):
    embed = std_embed()
    if len(args) == 0: 
        embed.add_field(name=":necktie: `class`", value="Lists supported classes", inline=False)
        embed.add_field(name=":unicorn: `race`", value="Lists supported races", inline=False)
        embed.add_field(name=":game_die: `rtd`", value="Roll Some Dice", inline=False)
    else: # parse the next arg

        # TODO move to individual helpers in a separate class
        if args[0] == 'class':
            embed.add_field(name=":necktie: `class`", value="type `?dnd class <class>` for information about a given class.\ne.g.: `?dnd class bard`", inline=False)
        elif args[0] == 'race':
            embed.add_field(name=":necktie: `race`", value="type `?dnd race <class>` for information about a given class.\ne.g.: `?dnd race elf`", inline=False)
        elif args[0] == 'prof':
            embed.add_field(name=":scales: `prof`", value="type `?dnd p <skill>` for information about a given proficiency.\ne.g.: `?dnd p skill-arcana`", inline=False)
        elif args[0] == 'rtd':
            embed.add_field(name=":game_die: `rtd`", value="type `?dnd rtd xdy` to roll x amount of dy\ng e.g. `?dnd 1d6` rolls 1d6", inline=False)
        else:
            embed.add_field(name="error", value="are you sure you typed the correct command?", inline=False)

    std_footer(embed)
    await ctx.send(embed=embed)

# Roll the Dice command
@client.command()
async def rtd(ctx, arg):
    # parse args here
    vals = arg.split("d")
    x = int(vals[0])
    y = int(vals[1])
    print(x, y)

    if x is None or y is None or x <= 0 or y <= 0:
        await ctx.send("invalid dice roll: try `?dnd xdy` where `x` and `y` are positive integers") 
    
    embed = std_embed()

    score = 0
    rolls = ""
    for i in range(x):
        curr_val = random.randint(1, y)
        score += curr_val
        if curr_val == 1:
            rolls += f"#{i+1}: **{curr_val}**/{y} -- oof crit. failure\n"
        elif curr_val == y:
            rolls += f"#{i+1}: **{curr_val}**/{y} -- max roll\n"
        else:
            rolls += f"#{i+1}: **{curr_val}**/{y}\n"

    embed.add_field(name=f":game_die: {x}d{y}", value=rolls, inline=False)
    embed.add_field(name="TOTAL: ", value=f"**{score}**/{x*y}", inline=False)
    std_footer(embed)

    await ctx.send(embed=embed)


# This should be entirely removed probably
@client.command()
async def meat(ctx, member=None):
    msg = None
    if member is None:
        if ctx.message.author.id == 560601419564974081:
            msg = f"{ctx.message.author.mention} {random.choice(MEAT['big'])}"
        else: 
            msg = f"{ctx.message.author.mention} {random.choice(MEAT['small'])}"   

    else: 
        if str(member) == "<@!560601419564974081>":
            msg = f"{member} {random.choice(MEAT['big'])}"
        else: 
            msg = f"{member} {random.choice(MEAT['small'])}"   
    
    await ctx.send(msg)

client.run(KEY)
