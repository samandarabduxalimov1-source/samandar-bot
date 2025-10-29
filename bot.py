import telebot
from telebot import types
from config import TOKEN, ADMIN_ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.first_name
    bot.send_message(message.chat.id, f"Salom, {user}! 👋\nMen Samandar yaratgan botman.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Buyruqlar:\n/start - Botni ishga tushirish\n/help - Yordam")

@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text.lower() == "salom":
        bot.send_message(message.chat.id, "Salom! Qandaysiz?")
    else:
        bot.send_message(message.chat.id, "Siz yozgan matnni tushunmadim 🤖")

if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.infinity_polling()
