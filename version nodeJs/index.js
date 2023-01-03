const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds] });
const dotenv = require('dotenv');

dotenv.config();

const menu = ["ไม่กินจร้า!","ผัดกะเพราหมู-ไก่","ข้าวผัดหมู-ไก่","ไข่เจียว","ไข่เจียวหมูสับ","ไข่ดาว","ปลากระป๋อง","มาม่าผัด","หมูทอด","ผัดหมู-ไก่ใส่พริก","ต้มจืดหมูสับ",
"ผัดหมู-ไก่ใส่กะหล่ำปลี","พะโล้","ผัดพริกไทยดำหมู-ไก่","ผัดกระเทียมหมู-ไก่","ผัดเผ็ดหมู-ไก่","แกงกะทิหมู-ไก่","ขนมจีน","แกงส้ม","ผัดหมี่เหลือง",
"ผัดผักรวม","ฉู่ฉี่","ยำไข่ต้ม","ยำไข่ดาว","ปลาทอด+น้ำพริกปลาทู","ข้าวเหนียวหมู","แกงไตปลา","ต้มหมูใบชะมวง","ผัดพริกหยวก",
"ไข่เจียวทรงเครื่อง","ไข่ตุ่น","ส้มตำ","ขาหมู","ผัดวุ้นเส้น","ข้าวผัดแหนม","ลาบหมู"];

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('interactionCreate', async interaction => {
  if (!interaction.isChatInputCommand()) return;
  if (interaction.commandName === 'menu') {   
    await interaction.reply(menu[Math.floor(Math.random() * menu.length)]);
  }
});

client.login(process.env.TOKEN);