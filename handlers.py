from bs4 import BeautifulSoup
import requests
import urllib
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, ParseMode
from telegram.ext import ConversationHandler
from glob import glob
from random import choice

from utillity import get_keyboard
# from mongodb import mdb, serch_or_save_user, save_user_anketa


# функция sms будут вызвана после отправки команды start
def sms(bot, update):
    # user = serch_or_save_user(mdb, bot.effective_user, bot.message)
    # print(user)
    print('Кто-то отправил команду start. Что мне делать?')
    bot.message.reply_text('Привет, {}! \nГотов помочь тебе в этом непростом деле, как быть "душой компании". Расскажи анекдот, произнеси тост. Да будет твой вечер самым лучшим. Да и ты - супер! Прошло все на 5? - РЕСПЕКТ АВТОРУ.'
                           .format(bot.message.chat.first_name), reply_markup=get_keyboard())


# Извлекаем тост
def get_tost(bot, update):
    receive = requests.get('http://rzhunemogu.ru/Widzh/Tost.aspx')
    page = BeautifulSoup(receive.text, "html.parser")
    find = page.select('#Label1')

    for text in find:
        page = (text.getText().strip())
        bot.message.reply_text('Слушай, {} тост от Андрюши\n'.format(bot.message.chat.first_name) + page)

# Извлекаем анекдот
def get_anekdot(bot, update):
    receive = requests.get('http://anekdotme.ru/random')
    page = BeautifulSoup(receive.text, "html.parser")
    find = page.select('.anekdot_text')
    for text in find:
        page = (text.getText().strip())
    bot.message.reply_text('Слушай, {} анекдотик от Андрюши\n'.format(bot.message.chat.first_name) + page)

def recpect(bot, update):
    bot.message.reply_text("https://money.yandex.ru/to/41001755475651")


# фукция parrot отвечает тем же сообщением, которое отправил пользователь
def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)




