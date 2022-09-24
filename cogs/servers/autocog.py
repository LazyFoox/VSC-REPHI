import discord
from discord.ext import commands
import config.data as data
import logging
from rich.logging import RichHandler
from rich.panel import Panel
from rich import print

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

log = logging.getLogger("rich")

class autocog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def testerror(self, ctx):
        try:
            print(1/0)
        except Exception:
            log.exeption("error!")

    @commands.command()
    async def load(self, ctx, cogsname=None):
        try:
            await self.bot.load_extension("cogs."+cogsname)
        except Exception:
            log.exeption("error!")

    @commands.command()
    async def unload(self, ctx, cogsname=None):
        await self.bot.unload_extension("cogs."+cogsname)

    @commands.command()
    async def reload(self, ctx, cogsname=None):
        await self.bot.reload_extension("cogs."+cogsname)


async def setup(bot):
    await bot.add_cog(autocog(bot))