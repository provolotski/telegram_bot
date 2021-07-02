import telebot
import security_chain

token = security_chain.token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,'Hello world')

@bot.message_handler(content_types=['location'])
def get_locations(message):
    print('i am here: ')
    print(message.location)

bot.polling()