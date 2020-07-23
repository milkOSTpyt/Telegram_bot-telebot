import telebot
from telebot import types
from func import forecast, openssource, belmeta
from pprint import pprint

bot = telebot.TeleBot('1054925361:AAEup4MWVjF9riW-kR5bFkyMk-4ak-EZKgo')


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weather = types.KeyboardButton('☀️Погода')
    opens = types.KeyboardButton('✏️OPENSSOURCE')
    belm = types.KeyboardButton('💼Belmeta')
    murkup.add(weather, opens, belm)
    bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=murkup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '☀️Погода':
        keys = types.InlineKeyboardMarkup()
        but_ost = types.InlineKeyboardButton(text="Островец", 
            callback_data='ostrovets-14630')
        but_mnsk = types.InlineKeyboardButton(text="Минск", 
            callback_data='minsk-4248')
        keys.add(but_ost, but_mnsk)
        bot.send_message(message.chat.id, 'Выберите город', reply_markup=keys)
    elif message.text == '✏️OPENSSOURCE':
        bot.send_message(message.chat.id, openssource())
    elif message.text == '💼Belmeta':
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text='Python', 
            callback_data='Python')
        but_2 = types.InlineKeyboardButton(text='Javascript', 
            callback_data='Javascript')
        but_3 = types.InlineKeyboardButton(text='Devops',callback_data='Devops')
        key.add(but_1, but_2, but_3)
        bot.send_message(message.chat.id, 'Выберите язык', reply_markup=key)


@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    if call.data == 'Python':
        bot.send_message(call.message.chat.id, belmeta(call.data))
    elif call.data == 'Javascript':
        bot.send_message(call.message.chat.id, belmeta(call.data))
    elif call.data == 'Devops':
        bot.send_message(call.message.chat.id, belmeta(call.data))
    elif call.data == 'ostrovets-14630':
        bot.send_message(call.message.chat.id, forecast(call.data))
    elif call.data == 'minsk-4248':
        bot.send_message(call.message.chat.id, forecast(call.data))


bot.polling()