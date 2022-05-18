import discord
from discord.ext import commands
from core.classes import Cog_Extension
class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(self.bot.latency)
def setup(bot):
    bot.add_cog(Main(bot))