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
        

async def setup(bot):
    await bot.add_cog(buttony(bot))