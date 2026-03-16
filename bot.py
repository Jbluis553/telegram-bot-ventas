import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os
from flask import Flask
from threading import Thread

# --- CONFIGURACIÓN PARA MANTENER EL BOT VIVO EN RENDER ---
app = Flask('')

@app.route('/')
def home():
    return "Bot de Ventas Online - Estatus: Activo"

def run():
    # Render asigna el puerto automáticamente
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ---------------------------------------------------------

# Usamos la variable de entorno que configuraste en el panel de Render
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

    elif "COMPRAR" in texto.upper():
        # Tu usuario de contacto para recibir los pagos
        bot.send_message(message.chat.id, "✅ **¡Excelente elección!**\n\nPor favor, contáctame aquí para finalizar tu compra: @Jbluis553")

    elif texto == "⬅ Volver":
        start(message)

    else:
        bot.send_message(message.chat.id, "Por favor, usa los botones del menú para navegar.")

if __name__ == "__main__":
    print("Iniciando servidor web y polling del bot...")
    keep_alive() # Inicia el servidor Flask
    bot.infinity_polling()
