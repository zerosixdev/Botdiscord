import os
import discord
import random
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

@bot.command()
async def random_message(ctx):
    messages = [
        "Hello there!",
        "How are you today?",
        "Here's a random message!",
        "Have a great day!",
        "Stay positive and happy!"
    ]
    response = random.choice(messages)
    await ctx.send(response)

bot.run(os.environ["DISCORD_TOKEN"])
