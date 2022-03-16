import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def waiter(self, ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)

    @commands.command()
    async def haha(self, ctx):
        pic = discord.File('D:\\Users\\USER\\Documents\\GitHub\\Waiter_01\\picture\\WeChat Image_20220314204529.png')
        await ctx.send(file= pic)

    @commands.command()
    async def club(self, ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))