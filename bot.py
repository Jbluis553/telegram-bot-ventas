import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os
from flask import Flask
from threading import Thread

# --- 1. SERVIDOR WEB PARA RENDER ---
app = Flask('')

@app.route('/')
def home():
    return "Bot de Ventas Online - Estatus: Live"

def run():
    # Render asigna el puerto en la variable PORT automáticamente
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Iniciamos el hilo web antes que el bot
t = Thread(target=run)
t.daemon = True
t.start()
# ----------------------------------

# Configuración del Bot usando tu variable de entorno
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

    elif "COMPRAR" in texto.upper():
        bot.send_message(message.chat.id, "✅ **Pedido recibido**\n\nContacta aquí para pagar:\nhttps://t.me/Jbluis553", parse_mode="Markdown")

    elif texto == "⬅ Volver":
        start(message)
    else:
        bot.send_message(message.chat.id, "Usa los botones del menú.")

if __name__ == "__main__":
    print("Servidor web y Bot iniciados...")
    bot.infinity_polling()
