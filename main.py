import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

class EveryThingBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        await self.change_presence(status=discord.Status.online,
                                activity=discord.Game("En développement  ..."))
        print(f"{self.user.display_name} is ready !")


EveryThing = EveryThingBot()
EveryThing.run(os.getenv("TOKEN"))