import telebot
from flask import Flask, request
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Salom men  ishlayapman 🚀")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.stream.read().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://SENING-LINKING.onrender.com/' + TOKEN)
    return "Webhook o‘rnatildi!", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
