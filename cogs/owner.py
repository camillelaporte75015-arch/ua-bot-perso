import discord
from discord import app_commands
from discord.ext import commands

owners = []

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="owner_add")
    async def owner_add(self, interaction: discord.Interaction, user: discord.User):
        owners.append(user.id)
        await interaction.response.send_message("Owner ajouté")

async def setup(bot):
    await bot.add_cog(Owner(bot))
