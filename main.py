import os
import discord
import aiohttp
import random
from discord.ext import commands
from forex_python.converter import CurrencyRates

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

currency_rates = CurrencyRates()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.reply('pong')

@bot.command()
async def hello(ctx):
    await ctx.reply("Choo choo! 🚅")

@bot.command()
async def menu(ctx):
    messages = [
        "ไม่กินจร้า!", "ผัดกะเพราหมู-ไก่", "ข้าวผัดหมู-ไก่", "ไข่เจียว",
        "ไข่เจียวหมูสับ", "ไข่ดาว", "ปลากระป๋อง", "มาม่าผัด", "หมูทอด",
        "ผัดหมู-ไก่ใส่พริก", "ต้มจืดหมูสับ", "ผัดหมู-ไก่ใส่กะหล่ำปลี", "พะโล้",
        "ผัดพริกไทยดำหมู-ไก่", "ผัดกระเทียมหมู-ไก่", "ผัดเผ็ดหมู-ไก่",
        "แกงกะทิหมู-ไก่", "ขนมจีน", "แกงส้ม", "ผัดหมี่เหลือง", "ผัดผักรวม",
        "ฉู่ฉี่", "ยำไข่ต้ม", "ยำไข่ดาว", "ปลาทอด+น้ำพริกปลาทู", "ข้าวเหนียวหมู",
        "แกงไตปลา", "ต้มหมูใบชะมวง", "ผัดพริกหยวก", "ไข่เจียวทรงเครื่อง",
        "ไข่ตุ่น", "ส้มตำ", "ขาหมู", "ผัดวุ้นเส้น", "ข้าวผัดแหนม", "ลาบหมู"
    ]
    response = random.choice(messages)
    await ctx.reply(response)

@bot.command()
async def btc(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coindesk.com/v1/bpi/currentprice.json') as response:
            data = await response.json()
            usd_rate = float(data["bpi"]["USD"]["rate"].replace(',', ''))
            thb_rate = currency_rates.convert('USD', 'THB', usd_rate)
            thb_rate = round(thb_rate, 2)
    await ctx.reply(f"<:Bitcoin1:1053606653309747210> Current Price Is {thb_rate} Thai Baht")

bot.run(os.environ["DISCORD_TOKEN"])
