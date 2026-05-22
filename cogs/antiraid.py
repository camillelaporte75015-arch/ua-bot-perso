from discord.ext import commands

class AntiRaid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot:
            await member.kick(reason="Anti bot")

async def setup(bot):
    await bot.add_cog(AntiRaid(bot))
