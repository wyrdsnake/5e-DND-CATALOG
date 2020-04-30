# bot.py

import discord
from discord.ext import commands, tasks
from conf import *

client = commands.Bot(command_prefix = '?dnd ')

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

@client.command(aliases =['should', 'backstab?', 'Should'])
async def should_I_Backstab(ctx):
    await ctx.send(f'yes')

@client.command(aliases =['peter_said_some_drunk_shit'])
async def peter_said_some_dumb_shit(ctx, amount = 2):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'knock it off pete "big gay" buttigieg ')


client.run(key)
