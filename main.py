import sys

import telebot
from telebot import types

import base

token = sys.argv[1]
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Добавить позицию",
                                      request_location=True))
    keyboard.add(types.KeyboardButton(text="Просмотреть локации"))
    keyboard.add(types.KeyboardButton(text="Забыть меня"))
    return keyboard


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = create_keyboard()
    bot.send_message(message.chat.id, text='Choose action', reply_markup=keyboard)
    # bot.send_message(message.chat.id, text='Choose action')


@bot.message_handler(commands=['list'])
def list_action(message):
    keyboard = create_keyboard()
    locations = base.get_location(base.get_user_id(message.from_user.id))
    for location in locations:
        bot.send_location(message.chat.id, location[1], location[0])
    bot.send_message(message.chat.id, text='Choose action', reply_markup=keyboard)


def forget_user(message):
    keyboard = create_keyboard()
    base.delete_user(base.get_user_id(message.from_user.id))
    bot.send_message(message.chat.id, text='you are deleted', reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def get_locations(message):
    userid = base.get_user_id(
        message.from_user.id) if base.get_user_id(
        message.from_user.id) != 0 else base.add_user(message.from_user.id, message.from_user.first_name,
                                                      message.from_user.username)
    base.add_location(userid, message.location.longitude, message.location.latitude)
    keyboard = create_keyboard()
    bot.send_message(message.chat.id, text='location added', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def query_handler(message):
    if message.text == 'Просмотреть локации':
        list_action(message)
    if message.text == 'Забыть меня':
        forget_user(message)


bot.polling()
