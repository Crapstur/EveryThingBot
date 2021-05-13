import discord
import os

from discord.ext import commands
from art import *

class Example(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    # =================================== EVENTS ================================== #
    @commands.Cog.listener()
    async def on_ready(self):
        os.system("clear")
        print(text2art("EveryThingBot"))
        print(f"Bot is online !")
        
        
    # ================================== COMMANDS ================================= #
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong !')
        
        
def setup(bot):
    bot.add_cog(Example(bot))