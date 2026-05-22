import discord
from discord import app_commands
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="avatar", description="Voir avatar")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user
        await interaction.response.send_message(member.display_avatar.url)

    @app_commands.command(name="say", description="Faire parler le bot")
    async def say(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message)

    @app_commands.command(name="mp", description="Envoyer MP")
    async def mp(self, interaction: discord.Interaction, member: discord.Member, message: str):
        await member.send(message)
        await interaction.response.send_message("MP envoyé", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Utility(bot))
