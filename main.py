import telebot
from setuptools.command.rotate import rotate
from  telebot import types

import security_chain

token = security_chain.token

bot = telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button_geo = types.InlineKeyboardButton(text="add", #callback_data="add",
                                  request_location=True)
    button_list = types.InlineKeyboardButton(text="list", callback_data="list"
                                       )
    buttons = [button_geo, button_list]


    keyboard.add(*buttons)
    return  keyboard

@bot.message_handler(commands=['start','help','list'])
def send_welcome(message):
    print(message)
    keyboard =create_keyboard()
    bot.send_message(message.chat.id, text='Choose action', reply_markup=keyboard)







@bot.message_handler(content_types=['location'])
def get_locations(message):
    print('i am here: ')
    print(message.location)

bot.polling()