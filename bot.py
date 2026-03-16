import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os
from flask import Flask
from threading import Thread

# --- SERVIDOR PARA RENDER ---
app = Flask('')
@app.route('/')
def home():
    return "Bot en línea"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

t = Thread(target=run)
t.daemon = True
t.start()
# ----------------------------

TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("🛒 Ver productos")
    markup.add(btn1)
    bot.send_message(message.chat.id, "👋 ¡Hola! Bienvenido.\nPresiona el botón para ver el catálogo.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text

    if texto == "🛒 Ver productos":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton("📘 Ebook $5")
        btn2 = KeyboardButton("🎨 Logo $10")
        btn3 = KeyboardButton("🌐 Página web $50")
        btn4 = KeyboardButton("⬅ Volver")
        markup.add(btn1, btn2)
        markup.add(btn3)
        markup.add(btn4)
        bot.send_message(message.chat.id, "💰 **Productos:**", reply_markup=markup, parse_mode="Markdown")

    # AQUÍ ESTÁ LA CORRECCIÓN: Nombres exactos como en los botones
    elif texto == "📘 Ebook $5":
        bot.send_message(message.chat.id, "📘 **Ebook Estrategias Digitales**\nPrecio: $5\n\nEscribe: COMPRAR EBOOK")

    elif texto == "🎨 Logo $10":
        bot.send_message(message.chat.id, "🎨 **Diseño de Logo**\nPrecio: $10\n\nEscribe: COMPRAR LOGO")

    elif texto == "🌐 Página web $50":
        bot.send_message(message.chat.id, "🌐 **Página Web**\nPrecio: $50\n\nEscribe: COMPRAR WEB")

    elif "COMPRAR" in texto.upper():
        bot.send_message(message.chat.id, "✅ **Pedido recibido.** Contacta aquí:\nhttps://t.me/Jbluis553")

    elif texto == "⬅ Volver":
        start(message)
    else:
        bot.send_message(message.chat.id, "Usa los botones del menú para navegar.")

if __name__ == "__main__":
    bot.infinity_polling()
