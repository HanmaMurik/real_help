from telebot import types

def button():
    kb = types.ReplyKeyboardMarkup()

    help_button = types.KeyboardButton('/help')

    kb.add(help_button)

    return kb