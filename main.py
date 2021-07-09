import sys

import telebot
from telebot import types

import base

token = sys.argv[1]
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button_geo = types.InlineKeyboardButton(text="add",  # callback_data="add",
                                            request_location=True)
    button_list = types.InlineKeyboardButton(text="list", callback_data="list")
    buttons = [button_geo, button_list]
    keyboard.add(*buttons)
    return keyboard


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = create_keyboard()
    #    bot.send_message(message.chat.id, text='Choose action', reply_markup=keyboard)
    bot.send_message(message.chat.id, text='Choose action')


@bot.message_handler(commands=['list'])
def send_welcome(message):
    keyboard = create_keyboard()
    #    bot.send_message(message.chat.id, text='Choose action', reply_markup=keyboard)
    locations  =  base.getLocation(base.getUserId(message.from_user.id))
    for location in locations:
        print(location[0])
        bot.send_location(message.chat.id,location[1], location[0])


@bot.message_handler(content_types=['location'])
def get_locations(message):
    print('i am here: ')
    userid = base.addUser(message.from_user.id, message.from_user.first_name,
                          message.from_user.username) if base.getUserId(message.from_user.id) == 0 else base.getUserId(
        message.from_user.id)
    base.addLocation(userid, message.location.longitude, message.location.latitude)
    print(f'userid is {userid}')
    print(message.location)


bot.polling()
