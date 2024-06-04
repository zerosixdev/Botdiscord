# This example requires the 'message_content' privileged intents

import os
import random
import requests
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

menu = [
    "ไม่กินจร้า!", "ผัดกะเพราหมู-ไก่", "ข้าวผัดหมู-ไก่", "ไข่เจียว",
    "ไข่เจียวหมูสับ", "ไข่ดาว", "ปลากระป๋อง", "มาม่าผัด", "หมูทอด",
    "ผัดหมู-ไก่ใส่พริก", "ต้มจืดหมูสับ", "ผัดหมู-ไก่ใส่กะหล่ำปลี", "พะโล้",
    "ผัดพริกไทยดำหมู-ไก่", "ผัดกระเทียมหมู-ไก่", "ผัดเผ็ดหมู-ไก่",
    "แกงกะทิหมู-ไก่", "ขนมจีน", "แกงส้ม", "ผัดหมี่เหลือง", "ผัดผักรวม",
    "ฉู่ฉี่", "ยำไข่ต้ม", "ยำไข่ดาว", "ปลาทอด+น้ำพริกปลาทู", "ข้าวเหนียวหมู",
    "แกงไตปลา", "ต้มหมูใบชะมวง", "ผัดพริกหยวก", "ไข่เจียวทรงเครื่อง",
    "ไข่ตุ่น", "ส้มตำ", "ขาหมู", "ผัดวุ้นเส้น", "ข้าวผัดแหนม", "ลาบหมู"
]

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
async def menu(ctx):
    await message.reply("<:food:1053608403576037506>" + " เมนูสุ่มได้แก่ : " + random.choice(menu))


bot.run(os.environ["DISCORD_TOKEN"])
