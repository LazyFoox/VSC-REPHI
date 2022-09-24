import discord
from discord.ext import commands
from discord.ui import Button, View, Select

class buttony(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def button(self, ctx):
        button = Button(label="click me!", style=discord.ButtonStyle.green)
        async def button_callback(interaction):
            await interaction.response.edit_message(content="heh you're cute now", view=None)
            await interaction.followup.send("hehe cute!")
        button.callback = button_callback
        view = View()
        view.add_item(button)
        await ctx.send("sup", view=view)

    @commands.command()
    async def google(self, ctx):
        view = View()
        view.add_item(discord.ui.Button(label="click here!", url="https://google.com"))
        await ctx.send(view=view)

    @commands.command()
    async def selected(self, ctx):
        select = Select(
            placeholder="what word you wanna say",
            options=[
                discord.SelectOption(label="floofy", description="so cute furs!"),
                discord.SelectOption(label="cuddle", description="snuzzle?"),
                discord.SelectOption(label="got to go", description="endy")
            ])
        async def my_callback(interaction: discord.Interaction):
            if interaction.user.id == ctx.author.id:
                await interaction.followup.send(select.values[0])
        select.callback = my_callback
        view = View()
        view.add_item(select)
        await ctx.send("what do i say", view=view)
        

async def setup(bot):
    await bot.add_cog(buttony(bot))