// Bot Telegram starter — Telegraf (Node.js)
// Install : npm install   |   Jalankan: node bot.js   (token di .env)
require('dotenv').config();
const { Telegraf } = require('telegraf');

const bot = new Telegraf(process.env.BOT_TOKEN); // jangan hardcode token

bot.start((ctx) => ctx.reply(`Halo ${ctx.from.first_name}! Bot aktif ✅ Ketik /help`));
bot.help((ctx) => ctx.reply('/start — mulai\n/id — lihat ID kamu\nKirim teks apa saja — akan kubalas (echo).'));
bot.command('id', (ctx) => ctx.reply(`User ID: ${ctx.from.id}\nChat ID: ${ctx.chat.id}`));
bot.on('text', (ctx) => ctx.reply(ctx.message.text));

bot.launch();
console.log('Bot jalan... Ctrl+C untuk berhenti');
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
