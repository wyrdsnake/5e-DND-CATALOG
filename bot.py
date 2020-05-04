# bot.py

import discord
from discord.ext import commands, tasks
import requests
from conf import *

client = commands.Bot(command_prefix = '?dnd ')
client.remove_command('help')

@client.event
async def on_ready():
    print('Time to roll.')


@client.event 
async def on_member_join(member):
    print(f'{member} has joined a server. ')


@client.event
async def on_memeber_remove(member):
    print(f'{member} has left a server')


@client.command()
#context(ctx) is automatically pased through command
async def ping(ctx):
    await ctx.send(f'Pong! ping = {round(client.latency *1000)} ms')

# test dialogue messages
@client.command(aliases =['should', 'backstab?', 'Should'])
async def should_I_Backstab(ctx):
    await ctx.send(f'yes')


@client.command(aliases=['p', 'proficiencies'])
async def _prof(ctx):
    embed=discord.Embed(title="**Calligula's Compendium**")
    
    res = requests.get('http://www.dnd5eapi.co/api/proficiencies/')
    res_json = res.json()
    d = dict(res_json)

    profs = []
    for n in d['results']:
        embed.add_field(name=n, value="idrk what u expected fuckwhite", inline=True)

    embed.set_footer(text="Support Calligula | PHB | poo poo pee pee")
    await ctx.send(embed=embed)

@client.command(aliases=['i'])
async def info(ctx):
    embed=discord.Embed(title="**Calligula's Compendium**", color=0xEA4246, description="@Ethan, probably put a better desc. of what the bot is supposed to do here.")
    embed.add_field(name="Written", value="@wyrdsnake\n@MurphyPone\n@Kabir")
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")
    embed.add_field(name="Invite", value="TODO")
    await ctx.send(embed=embed)

@client.command(name="help", aliases=['h'])
async def help(ctx, *args):
    if len(args) == 0: 
        embed=discord.Embed(title="**Calligula's Compendium**", color=0xEA4246)
        embed.add_field(name=":necktie: `class`", value="lists supported classes", inline=False)
        embed.add_field(name=":unicorn: `race`", value="lists supported races", inline=False)
        embed.add_field(name=":game_die: `rtd`", value="moderate rtd", inline=False)
        await ctx.send(embed=embed)
    else: # parse the next arg

        # TODO move to individual helpers in a separate class
        if args[0] == 'class':
            embed=discord.Embed(title="**Calligula's Compendium**", color=0xEA4246)
            embed.add_field(name=":necktie: `class`", value="type `?dnd class <class>` for information about a given class.\ne.g.: `?dnd class bard`", inline=False)
            embed.set_footer(text="Support Calligula | PHB | poo poo pee pee")
            await ctx.send(embed=embed)
        elif args[0] == 'race':
            embed=discord.Embed(title="**Calligula's Compendium**", color=0xEA4246)
            embed.add_field(name=":necktie: `race`", value="type `?dnd race <class>` for information about a given class.\ne.g.: `?dnd race elf`", inline=False)
            embed.set_footer(text="Support Calligula | PHB | poo poo pee pee")
            await ctx.send(embed=embed)
        elif args[0] == 'prof':
            embed=discord.Embed(title="**Calligula's Compendium**", color=0xEA4246)
            embed.add_field(name=":scales: `prof`", value="type `?dnd p <skill>` for information about a given proficiency.\ne.g.: `?dnd p skill-arcana`", inline=False)
            embed.set_footer(text="Support Calligula | PHB | poo poo pee pee")
            await ctx.send(embed=embed)
        elif args[0] == 'rtd':
            embed=discord.Embed(title="**Calligula's Compendium**", color=0xEA4246)
            embed.add_field(name=":game_die: `rtd`", value="type `?dnd rtd xdy` to roll x amount of dy\ng e.g. `?dnd 1d6` rolls 1d6", inline=False)
            embed.set_footer(text="Support Calligula | PHB | poo poo pee pee")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="**Calligula's Compendium**", color=0xEA4246)
            embed.add_field(name="error", value="are you sure you typed the correct command?", inline=False)
            embed.set_footer(text="Support Calligula | PHB | poo poo pee pee")
            await ctx.send(embed=embed)

client.run(KEY)
