import os
import discord

from discord.ext import commands
from dotenv import load_dotenv
from art import *

load_dotenv(dotenv_path="config")

bot = commands.Bot(command_prefix="!")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print(f'Cogs {extension} load.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print(f'Cogs {extension} unload.')
    
@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print(f'Cogs {extension} reload.')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv("TOKEN"))