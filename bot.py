import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os
from flask import Flask
from threading import Thread

# --- 1. SERVIDOR WEB PARA RENDER (INDISPENSABLE) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot de Ventas Online - Estatus: Activo y Live"

def run():
    # Render asigna el puerto automáticamente en la variable PORT
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Iniciamos el hilo del servidor web ANTES que el bot
t = Thread(target=run)
t.daemon = True  # Permite que el hilo se cierre si el proceso principal muere
t.start()
# --------------------------------------------------

# --- 2. CONFIGURACIÓN DEL BOT ---
# Lee el Token de la variable de entorno que configuraste en Render
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

# MENÚ PRINCIPAL
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("🛒 Ver productos")
    markup.add(btn1)
    
    bot.send_message(
        message.chat.id, 
        "👋 ¡Hola! Bienvenido a mi bot de ventas.\n\n"
        "Presiona el botón de abajo para ver el catálogo.", 
        reply_markup=markup
    )

# RESPUESTAS DEL BOT
@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text

    # Catálogo de productos
    if texto == "🛒 Ver productos":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton("📘 Ebook $5")
        btn2 = KeyboardButton("🎨 Logo $10")
        btn3 = KeyboardButton("🌐 Página web $50")
        btn4 = KeyboardButton("⬅ Volver")
        
        markup.add(btn1, btn2)
        markup.add(btn3)
        markup.add(btn4)
        bot.send_message(message.chat.id, "💰 **Catálogo de productos:**", reply_markup=markup, parse_mode="Markdown")

    elif texto == "📘 Ebook $5":
        bot.send_message(message.chat.id, "📘 **Ebook Estrategias Digitales**\n\nPrecio: $5 USD\n\nPara comprar, escribe: `COMPRAR EBOOK`", parse_mode="Markdown")

    elif texto == "🎨 Logo $10":
        bot.send_message(message.chat.id, "🎨 **Diseño de Logo Pro**\n\nPrecio: $10 USD\n\nPara comprar, escribe: `COMPRAR LOGO`", parse_mode="Markdown")

    elif texto == "🌐 Página web $50":
        bot.send_message(message.chat.id, "🌐 **Landing Page Personalizada**\n\nPrecio: $50 USD\n\nPara comprar, escribe: `COMPRAR WEB`", parse_mode="Markdown")

    # Detección flexible de compra (no importa si es minúscula o mayúscula)
    elif "COMPRAR" in texto.upper():
        bot.send_message(
            message.chat.id, 
            "✅ **¡Excelente elección!**\n\nHe recibido tu pedido. Por favor, contáctame aquí directamente para finalizar el pago y la entrega:\n\n👉 https://t.me/Jbluis553",
            parse_mode="Markdown"
        )

    elif texto == "⬅ Volver":
        start(message)

    else:
        bot.send_message(message.chat.id, "Por favor, usa los botones del menú para navegar.")

# --- 3. INICIO DEL POLLING ---
if __name__ == "__main__":
    print("Servidor web iniciado en puerto 10000")
    print("Bot escuchando mensajes de Telegram...")
    bot.infinity_polling()
