import dotenv
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Bot

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

CHAT_ID = '6565697665'

# async def start(update: Update, context):
#     CHAT_ID = update.effective_chat.id
#     await update.message.reply_text(f"Tu CHAT_ID es: {CHAT_ID}")
    
# app = Application.builder().token(BOT_TOKEN).build()
# app.add_handler(CommandHandler('start', start))

# print("Envía /start al bot en Telegram para obtener tu CHAT_ID.")
# app.run_polling()

def send_message(message):
    bot = Bot(token=BOT_TOKEN)
    bot.sendMessage(chat_id=CHAT_ID, text=message)
    print('Message sent successfully')