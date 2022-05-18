from random import random
from urllib import response
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time
import asyncio
import json
import random
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)
class React(Cog_Extension):
    @commands.command()
    async def emoji(self,ctx):
        rdp=random.choice(jdata['emo'])
        await ctx.send(rdp)
    @commands.command()
    async def 紅富士(self,ctx):
        await ctx.send(jdata['apple'])
    @commands.command()
    async def 旋轉(self,ctx):
        await ctx.send(jdata['spin1016'])
    @commands.command()
    async def sear(self,ctx):
        def check(nam):
            return nam.author ==ctx.author and nam.channel == ctx.message.channel
        await ctx.send('你要查誰\n')
        for i in range(0,1):
            response = await self.bot.wait_for('message',check=check)
            try:
                sear=str(response.content)
            except:
                await ctx.send("你要查誰?")

            await ctx.send(jdata['sear1']+sear+jdata['sear2'])
def setup(bot):
    bot.add_cog(React(bot))