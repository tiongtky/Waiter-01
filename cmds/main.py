from datetime import datetime
from re import A
from sqlite3 import Timestamp
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import json


class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('Hi~')

    @commands.command()
    async def host(self, ctx):
        embed=discord.Embed(title="Author of Job博士's Club", description="The owner of the bot", color=0x71eefe, timestamp= datetime.datetime.utcnow())
        embed.set_author(name="Job博士",url="https://www.facebook.com/tiongtky", icon_url="https://media4.giphy.com/media/VpysUTI25mTlK/giphy.gif")
        embed.set_thumbnail(url="https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/tenor_1.gif")
        embed.add_field(name="Real Name", value="Tiong_Kwong_Yew", inline=True)
        embed.add_field(name="Date of Birth", value="15-02-1995", inline=True)
        embed.add_field(name="Other Information", value="!   SECRET   !", inline=False)
        embed.set_footer(text="click the name")
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    async def time(self, ctx):
      B = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      await ctx.send(B)

    @commands.command()
    async def utctime(self, ctx):
      C = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
      await ctx.send(C)


def setup(bot):
    bot.add_cog(Main(bot))