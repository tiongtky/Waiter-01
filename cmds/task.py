from ast import Num
import numbers
from textwrap import indent
from time import time
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime


class task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(952902772280426516)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                with open('setting.json', 'r', encoding='utf8') as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata['time'] and self.counter != 3:
                    await self.channel.send('Time UP!')
                    self.counter = self.counter + 1
                    await asyncio.sleep(3)  #s
                else:

                    await asyncio.sleep(1)  #s
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def setchannel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'set channel:{self.channel.mention}')

    @commands.command()
    async def settime(self, ctx, time):
        self.counter = 0
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata["time"] = time
        with open('setting.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
        await ctx.send(f'Time:{time} has been set!')


def setup(bot):
    bot.add_cog(task(bot))
