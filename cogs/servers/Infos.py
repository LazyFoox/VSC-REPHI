import discord
from discord.ext import commands

class infoslist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, user:discord.Member=None): #self, ctx, user=discord.Member=None
        nickname = " " 
        if user is None:
            user = ctx.author
        if user.name != user.display_name:
            nickname = f"**Nickname**: {user.display_name}" 
        embed = discord.Embed(timestamp=ctx.message.created_at, title="User", description=f"**UserName**: {user.name}#{user.discriminator}\n{nickname}")
        embed.set_author(name=f"{user.display_name}", icon_url=user.avatar.url)
        embed.add_field(name="Member Guild", value=f"**ID**: {user.id}\n**Status**: {user.status} | {user.activity}\n**Top Role**: {user.top_role}")
        embed.add_field(name="Member Stats", value="**Joined**: {}\n**Created**: {}".format(user.joined_at.strftime("%d %b %Y %H:%M"), user.created_at.strftime("%d %b %Y %H:%M")))
        embed.set_thumbnail(url=user.avatar.url)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def guildinfo(self, ctx):
        guild = ctx.guild
        embed=discord.Embed(timestamp=ctx.message.created_at, title="Owner info", description=f"**Server name**: {guild.name}\n**Owner**: {guild.owner.name}#{guild.owner.discriminator}")
        embed.set_thumbnail(url=guild.icon.url)
        embed.set_footer(text=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(infoslist(bot))