import discord

from discord.ext import commands

class Example(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is online !")
        
        
    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong !')
        
     
def setup(bot):
    bot.add_cog(Example(bot))