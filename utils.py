import discord

# creates a standard message
def std_embed():
    embed=discord.Embed(title="**Calligula's Compendium**", color=0xEA4246, description="@Ethan, probably put a better desc. of what the bot is supposed to do here.")
    embed.set_footer(text="Support Calligula | PHB | Invite")
    return embed