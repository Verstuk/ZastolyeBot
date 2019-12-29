# Импортируем необходимые компоненты
# import kwargs as kwargs
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from setting import TG_TOKEN, TG_API_URL
from handlers import *
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


#Создаем фнукцию main, с помощью которой соеденяемся с сервисом telegram

def main():
    my_bot = Updater(TG_TOKEN, TG_API_URL, use_context=True)
    logging.info('Start bot')

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('НАЧАТЬ'), sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('ТОСТ'), get_tost))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('АНЕКДОТ'), get_anekdot))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('РЕСПЕКТ АВТОРУ'), recpect))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))
    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
