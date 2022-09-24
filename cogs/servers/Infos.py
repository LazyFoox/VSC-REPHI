import discord
from discord.ext import commands

class infoslist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guildinfo(self, ctx):
        guild = ctx.guild
        embed=discord.Embed(timestamp=ctx.message.created_at, title="Owner info", description=f"**Server name**: {guild.name}\n**Owner**: {guild.owner.name}#{guild.owner.discriminator}")
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(infoslist(bot))