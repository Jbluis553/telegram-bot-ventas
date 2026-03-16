import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# TOKEN del bot
TOKEN = "8679602699:AAHNDRLLbEFzojJDYozkZYLoS08xmXQEHn0"

bot = telebot.TeleBot(TOKEN)

# MENÚ PRINCIPAL
@bot.message_handler(commands=['start'])
def start(message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = KeyboardButton("🛒 Ver productos")

    markup.add(btn1)

    bot.send_message(
        message.chat.id,
        "👋 Bienvenido a nuestro bot de ventas\n\n"
        "Presiona el botón para ver productos",
        reply_markup=markup
    )


# RESPUESTAS DEL BOT
@bot.message_handler(func=lambda message: True)
def responder(message):

    texto = message.text

    # MENÚ DE PRODUCTOS
    if texto == "🛒 Ver productos":

        markup = ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = KeyboardButton("📘 Ebook $5")
        btn2 = KeyboardButton("🎨 Logo $10")
        btn3 = KeyboardButton("🌐 Página web $50")
        btn4 = KeyboardButton("⬅ Volver")

        markup.add(btn1, btn2)
        markup.add(btn3)
        markup.add(btn4)

        bot.send_message(
            message.chat.id,
            "💰 Productos disponibles",
            reply_markup=markup
        )

    # PRODUCTO 1
    elif texto == "📘 Ebook $5":

        bot.send_message(
            message.chat.id,
            "📘 Ebook para ganar dinero online\n\n"
            "Precio: $5\n\n"
            "Para comprar escribe: COMPRAR EBOOK"
        )

    # PRODUCTO 2
    elif texto == "🎨 Logo $10":

        bot.send_message(
            message.chat.id,
            "🎨 Diseño de logo profesional\n\n"
            "Precio: $10\n\n"
            "Para comprar escribe: COMPRAR LOGO"
        )

    # PRODUCTO 3
    elif texto == "🌐 Página web $50":

        bot.send_message(
            message.chat.id,
            "🌐 Creación de página web\n\n"
            "Precio: $50\n\n"
            "Para comprar escribe: COMPRAR WEB"
        )

    # COMPRA
    elif "COMPRAR" in texto:

        bot.send_message(
            message.chat.id,
            "✅ Pedido recibido\n\n"
            "Para pagar contacta aquí:\n"
            "https://t.me/TU_USUARIO"
        )

    # VOLVER
    elif texto == "⬅ Volver":

        markup = ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = KeyboardButton("🛒 Ver productos")

        markup.add(btn1)

        bot.send_message(
            message.chat.id,
            "Menú principal",
            reply_markup=markup
        )

    else:

        bot.send_message(
            message.chat.id,
            "Selecciona una opción del menú"
        )


print("Bot funcionando...")

bot.infinity_polling()
