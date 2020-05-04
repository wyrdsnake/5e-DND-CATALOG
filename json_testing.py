import requests
import json

url = 'http://www.dnd5eapi.co/api/races/'
res = requests.get(url)
res_json = res.json()
print(list(res_json))

d = dict(res_json)

print(d['results'])
names = []
for n in d['results']:
    names.append(n['index'])

print(names)


# # Lists proficiencies
# @client.command(aliases=['p', 'proficiencies'])
# async def _prof(ctx):
#     embed = std_embed()
    
#     res = requests.get('http://www.dnd5eapi.co/api/proficiencies/')
#     res_json = res.json()
#     d = dict(res_json)

#     profs = []
#     for n in d['results']:
#         embed.add_field(name=n, value="idrk what u expected", inline=True)

#     embed.add_field(name="Links", value="![Support Calligula](https://www.google.com) | [PHB]({}) | [Invite]({})".format("google.com","google.com" ) , inline=False)
#     await ctx.send(embed=embed)