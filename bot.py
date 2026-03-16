import telebot

TOKEN = "8679602699:AAF9K5-4sfdlQ4rJV9K069otQCyzXYUHrnY"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    texto = (
        "👋 Bienvenido a mi bot\n\n"
        "Escribe MENU para ver servicios"
    )
    bot.send_message(message.chat.id, texto)

@bot.message_handler(func=lambda message: True)
def responder(message):

    msg = message.text.lower()

    if msg == "menu":
        bot.send_message(
            message.chat.id,
            "💰 SERVICIOS DISPONIBLES\n\n"
            "1 - Diseño de Logo\n"
            "2 - Página Web\n"
            "3 - Automatización\n\n"
            "Escribe el número del servicio"
        )

    elif msg == "1":
        bot.send_message(
            message.chat.id,
            "🎨 Logo profesional\nPrecio: $10\n\nEscribe COMPRAR"
        )

    elif msg == "2":
        bot.send_message(
            message.chat.id,
            "🌐 Página web\nPrecio: $50\n\nEscribe COMPRAR"
        )

    elif msg == "3":
        bot.send_message(
            message.chat.id,
            "🤖 Automatización\nPrecio: $30\n\nEscribe COMPRAR"
        )

    elif msg == "comprar":
        bot.send_message(
            message.chat.id,
            "💳 Para comprar escribe a:\n@tu_usuario\n\nPago por PayPal o transferencia"
        )

    else:
        bot.send_message(
            message.chat.id,
            "❓ No entendí el comando\nEscribe MENU"
        )

print("Bot funcionando...")
bot.infinity_polling()
