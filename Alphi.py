# !! CODED BY LAZYFOOX!!

import discord
from tinydb import TinyDB
from discord.ext import commands
import config.data as data
import config.colours as colours
import os
from rich import print
from rich.tree import Tree
from rich.text import Text
from rich.progress import track

#ha = TinyDB("data/ha.json")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=data.PREFIX, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print("started! hello worldy wodry")
    await load_extension()
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("pog lazyfoox using vsc pc"))

# cogs list
list = (
    "servers",
    "bots",
    "custom",
)

async def load_extension():
    liss = []
    tree = Tree(label="│")
    for lists in track((list), description="progressing."):
        tree1 = tree.add(lists)
        for filename in os.listdir("cogs/"+lists):
            if filename.endswith(".py"):
                try:
                    await bot.load_extension("cogs."+lists+f".{filename[:-3]}")
                    tree1.add(filename[:-3] + " !")
                except Exception as e:
                    # print(f"FAILUIRE {e}")
                    tree1.add(filename[:-3] + f" X [reverse red]{e}[/reverse red]")
    
    print(tree)


@bot.command()
async def dosomething(ctx):
    await ctx.send("I did something")


bot.run(data.TOKEN, reconnect=True)