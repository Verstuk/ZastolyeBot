from telegram import ReplyKeyboardMarkup, KeyboardButton

# Фунция создани клавиатуры и разметки
def get_keyboard():
    my_keyboard = ReplyKeyboardMarkup([['ТОСТ', 'АНЕКДОТ'],
                                       ['РЕСПЕКТ АВТОРУ','НАЧАТЬ']],
                                      resize_keyboard=True)  # Добавляем кнопку
    return my_keyboard