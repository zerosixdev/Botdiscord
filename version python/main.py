import discord
import random
import requests

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


class MyClient(discord.Client):
    async def on_ready(self):
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Hellozerosix Server"))
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content.startswith('btc'):
            response = requests.get(
            'https://api.coindesk.com/v1/bpi/currentprice.json')
            data = response.json()
            #print(data)
            await message.reply(
            "<:Bitcoin1:1053606653309747210> Current Price Is " +
            data["bpi"]["USD"]["rate"] + " US Dollar")

        if message.content.startswith('Btc'):
            response = requests.get(
            'https://api.coindesk.com/v1/bpi/currentprice.json')
            data = response.json()
            #print(data)
            await message.reply(
            "<:Bitcoin1:1053606653309747210> Current Price Is " +
            data["bpi"]["USD"]["rate"] + " US Dollar")

        if message.content.startswith('menu'):
            await message.reply("<:food:1053608403576037506>" +
                            " เมนูสุ่มได้แก่ : " + random.choice(menu))

        if message.content.startswith('Menu'):
            await message.reply("<:food:1053608403576037506>" +
                            " เมนูสุ่มได้แก่ : " + random.choice(menu))

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run("MTA2NTQ0MzU3MzAwMjE0MTc3Ng.Gb15u-.Q9X3rtpIQNlOGxYSQeoSim5xOGRV_3qNAZcF9s")
