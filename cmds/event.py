import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)
class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        b=0
        for i in range(0,len(jdata['inmu'])):
            if msg.content.find(jdata['inmu'][i]) !=-1 and msg.author != self.bot.user:
                if b==0:
                    await msg.channel.send(jdata['inmuele'])  
                    b=1  
        if b==0:
            if msg.content == "自裁" and msg.author != self.bot.user:
                await msg.channel.send(jdata['su'])
            elif msg.content[0]!='-'and msg.author != self.bot.user:
                await msg.channel.send('=========================')
def setup(bot):
    bot.add_cog(Event(bot))