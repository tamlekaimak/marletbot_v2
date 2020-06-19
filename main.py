import telebot
from telebot import types

botApi = "901255483:AAEV3UaDILEmQamHe-aCCkVLE_8RI2H2mfg"

bot = telebot.TeleBot(botApi)

print("Бот запущен!")

def send(chatid, message):
    try:
        bot.send_message(chatid, message, parse_mode= 'Markdown')
    except Exception as e:
        print(e)
        return False
    else:
        return True

@bot.message_handler(commands = ['start'])
def start(message):
    chatid = message.chat.id
    
    send(chatid, 'Привет, я каймак бот!')

@bot.message_handler(content_types = ['text'])
def taker(message):
    chatid = message.chat.id
    send(chatid, 'OK!')

bot.infinity_polling(True)
bot.polling()