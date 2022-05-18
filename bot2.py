import discord
from discord.ext import commands
import json
import os
import random
with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(">>Bot is online<<")
for fname in os.listdir('./cmds'):
    if fname.endswith('.py'):
        bot.load_extension(f'cmds.{fname[:-3]}')

if __name__== "__main__":
    bot.run(jdata['token'])
