import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os
from flask import Flask
from threading import Thread

# 1. Servidor para que Render no apague el bot
app = Flask('')
@app.route('/')
def home():
    return "Bot Online"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

t = Thread(target=run)
t.daemon = True
t.start()

# 2. Configuración del Bot
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("🛒 Ver productos"))
    bot.send_message(message.chat.id, "👋 ¡Bienvenido! Presiona el botón para ver el catálogo.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text
    if texto == "🛒 Ver productos":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("📘 Ebook $5"), KeyboardButton("🎨 Logo $10"))
        markup.add(KeyboardButton("🌐 Página web $50"), KeyboardButton("⬅ Volver"))
        bot.send_message(message.chat.id, "💰 **Catálogo:**", reply_markup=markup, parse_mode="Markdown")
    
    elif "COMPRAR" in texto.upper() or "$" in texto:
        bot.send_message(message.chat.id, "✅ **Pedido recibido.** Contacta aquí para pagar: https://t.me/Jbluis553")
    
    elif texto == "⬅ Volver":
        start(message)

if __name__ == "__main__":
    bot.infinity_polling()
