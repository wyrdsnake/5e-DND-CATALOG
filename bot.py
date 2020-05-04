# bot.py

import discord
from discord.ext import commands, tasks
import requests
from conf import *
from utils import *

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


## client commands
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! ping = {round(client.latency *1000)} ms')

# Sets a cron to change bot status every 5 minutes 
@tasks.loop(minutes=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(STATUSES)))

# Lists proficiencies
@client.command(aliases=['p', 'proficiencies'])
async def _prof(ctx):
    embed = std_embed()
    
    res = requests.get('http://www.dnd5eapi.co/api/proficiencies/')
    res_json = res.json()
    d = dict(res_json)

    profs = []
    for n in d['results']:
        embed.add_field(name=n, value="idrk what u expected", inline=True)

    embed.add_field(name="Links", value="![Support Calligula](https://www.google.com) | [PHB]({}) | [Invite]({})".format("google.com","google.com" ) , inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['i'])
async def info(ctx):
    embed = std_embed()
    embed.add_field(name="Written", value="@wyrdsnake\n@MurphyPone\n@Kabir")
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")
    embed.add_field(name="Invite", value="TODO")
    embed.add_field(name="Links", value="![Support Calligula](https://www.google.com) | [PHB]({}) | [Invite]({})".format("google.com","google.com" ) , inline=False)
    await ctx.send(embed=embed)

@client.command(name="help", aliases=['h'])
async def help(ctx, *args):
    embed = std_embed()
    if len(args) == 0: 
        embed.add_field(name=":necktie: `class`", value="lists supported classes", inline=False)
        embed.add_field(name=":unicorn: `race`", value="lists supported races", inline=False)
        embed.add_field(name=":game_die: `rtd`", value="moderate rtd", inline=False)
        embed.add_field(name="Links", value="![Support Calligula](https://www.google.com) | [PHB]({}) | [Invite]({})".format("google.com","google.com" ) , inline=False)
        await ctx.send(embed=embed)
        return 
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

    embed.add_field(name="Links", value="[Support Calligula](https://www.google.com) | [PHB]({}) | [Invite]({})".format("google.com","google.com" ) , inline=False)
    await ctx.send(embed=embed)

@client.command()
async def rtd(ctx, arg):
    # parse args here
    vals = arg.split("d")
    x = int(vals[0])
    y = int(vals[1])
    embed = std_embed()

    if x is None or y is None:
        await ctx.send("invalid args: try `?dnd xdy` where `x` and `y` are integers") 
    
    score = 0
    for i in range(x):
        curr_val = random.randint(1, y)
        score += curr_val
        if curr_val == 1:
            embed.add_field(name=f":game_die: {i}/{x}", value=f"{curr_val}/{y} -- oof crit. failure.", inline=False)
        elif curr_val == y:
            embed.add_field(name=f":game_die: {i}/{x}", value=f"{curr_val}/{y} -- Max roll baby", inline=False)
        else:
            embed.add_field(name=f":game_die: {i}/{x}", value=f"{curr_val}/{y}", inline=False)

    embed.add_field(name="TOTAL: ", value=f"{score}/{x*y}", inline=False)
    embed.add_field(name="Links", value="![Support Calligula](https://www.google.com) | [PHB]({}) | [Invite]({})".format("google.com","google.com" ) , inline=False)

    await ctx.send(embed=embed)


client.run(KEY)
