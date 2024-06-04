# This example requires the 'message_content' privileged intents

import os
import discord
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send("Choo choo! 🚅")

# @bot.command()
# async def menu(ctx):
#     await message.reply("<:food:1053608403576037506>" + " เมนูสุ่มได้แก่ : " + random.choice(menu))


bot.run(os.environ["DISCORD_TOKEN"])
