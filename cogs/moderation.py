import discord
from discord import app_commands
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Bannir un membre")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await member.ban(reason=reason)
        await interaction.response.send_message(f"🔨 {member} banni")

    @app_commands.command(name="clear", description="Supprimer messages")
    async def clear(self, interaction: discord.Interaction, amount: int):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message("🧹 Messages supprimés", ephemeral=True)

    @app_commands.command(name="timeout", description="Timeout un membre")
    async def timeout(self, interaction: discord.Interaction, member: discord.Member, seconds: int):
        await member.timeout(discord.utils.utcnow() + discord.timedelta(seconds=seconds))
        await interaction.response.send_message("⏱ Timeout appliqué")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
