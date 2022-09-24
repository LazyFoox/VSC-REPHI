import discord
from discord.ext import commands

class infoslist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guildinfo(self, ctx):
        guild = ctx.guild
        embed=discord.Embed(timestamp=ctx.message.created_at, title="Owner info", description=f"**Server name**: {guild.name}\n**Owner**: {guild.owner.name}#{guild.owner.discriminator}")
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_author(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(infoslist(bot))