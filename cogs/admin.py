import discord

from discord.ext import commands

class Admin(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    # =================================== EVENTS ================================== #
    # ============================================================================= #

        
    # ================================== COMMANDS ================================= #

    # Command !clear
    @commands.command(brief='Clear the channel')
    @commands.has_role("Admin")
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount + 1)
    # ============================================================================= #


    # =================================== ERROR =================================== #
    # Error command !clear
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingRole):
            await ctx.send("Tu doit avoir le rôle Admin pour faire cette commande.")
    # ============================================================================= #
def setup(bot):
    bot.add_cog(Admin(bot))