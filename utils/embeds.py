import discord

def embed(title, desc, color=0x2b2d31):
    return discord.Embed(title=title, description=desc, color=color)
