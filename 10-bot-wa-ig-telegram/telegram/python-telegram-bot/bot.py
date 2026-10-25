"""
Bot Telegram starter — python-telegram-bot v21+
Install : pip install -r requirements.txt
Isi     : copy .env.example -> .env, isi BOT_TOKEN dari @BotFather
Jalankan: python bot.py
Fitur   : /start  /help  /id  + membalas (echo) pesan teks biasa
"""
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()
TOKEN = os.environ["BOT_TOKEN"]  # sengaja error kalau belum diisi — jangan hardcode token

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Halo {update.effective_user.first_name}! Bot aktif ✅\nKetik /help untuk daftar perintah.")

async def help_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start — mulai\n/id — lihat ID Telegram kamu\nKirim teks apa saja — akan kubalas (echo).")

async def my_id(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    await update.message.reply_text(f"Nama: {u.first_name}\nUser ID: {u.id}\nChat ID: {update.effective_chat.id}")

async def echo(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("id", my_id))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot jalan... Ctrl+C untuk berhenti")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
