import os
from dotenv import load_dotenv

load_dotenv()

import telebot

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=["start"])
def hello(message):
    print("bot started...")
    bot.reply_to(message, f"Hello {message.from_user.first_name}\nhow are you")

@bot.message_handler(func=lambda message:True)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()