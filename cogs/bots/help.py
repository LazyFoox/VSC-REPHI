import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", description=";help (this is a beta commands. textholder)\n;guildinfo\n;button\n;google\n;selected")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(help(bot))