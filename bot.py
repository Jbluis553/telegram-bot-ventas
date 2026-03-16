import telebot

TOKEN = "8679602699:AAHNDRLLbEFzojJDYozkZYLoS08xmXQEHn0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"Hola 👋 escribe MENU")

@bot.message_handler(func=lambda m: True)
def menu(message):

    msg = message.text.lower()

    if msg == "menu":
        bot.reply_to(message,
        "SERVICIOS\n"
        "1 Logo $10\n"
        "2 Web $50")

bot.polling()
