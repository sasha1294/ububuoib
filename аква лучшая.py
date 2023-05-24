import telebot

bot = telebot.TeleBot('5684331901:AAEnqassWSzxZKYAZdaSL2QJMtKgu3_esYE')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>i facked your father</b>', parse_mode='html')


bot.polling(none_stop=True)
