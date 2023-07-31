import telebot, button_help

bot = telebot.TeleBot('6430626571:AAFeidgwfWkeo73p_jpDQ199BdJdG_BZH9s')


@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, 'Hi! choose your action', reply_markup=button_help.button())



@bot.message_handler(commands=['help'])

def help(message):
    bot.send_message(message.chat.id, 'If you have problems and you want to recourse, please, message to our admin, his contacts: @safarov_mirshod')
    bot.register_next_step_handler(message, help)

bot.polling(none_stop=True)
