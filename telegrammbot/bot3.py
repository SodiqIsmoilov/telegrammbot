import telebot
from telebot import types

bot = telebot.TeleBot("1160263369:AAHKmOAGPSqSz1B0N2idYT-Okw6Q3io1UI0")
# Info O`qituvchi

answer_teach = []
number_test = 0
data_base = {}
number_t = 0
info = ''

# Info Abitruyent


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn1 = types.KeyboardButton('O`qituvchi')
btn2 = types.KeyboardButton('Abitruyent')
markup.add(btn1, btn2)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Salom foydalanuvchi kim ekanligingizni tanlang ', reply_markup=markup)
    if message.text == 'O`qituvchi':
        bot.reply_to(message, 'Iltimos parolni kiriting ')
        bot.register_next_step_handler(message, teach_pas)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'O`qituvchi':
        bot.reply_to(message, 'Iltimos parolni kiriting ')
        bot.register_next_step_handler(message, teach_pas)

    #     O`qituvchining paroli


def teach_pas(message):
    try:
        if int(message.text) == 12345:
            bot.reply_to(message, 'Test nomerini jo`nating ')
            bot.register_next_step_handler(message, t_num)
        else:
            bot.reply_to(message, 'Parol noto`g`ri qaytadan kiriting !')
            bot.register_next_step_handler(message, teach_pas)
    except AttributeError:
        bot.reply_to(message.from_user.id, 'Parol noto`g`ri qaytadan kiriting !')
        bot.register_next_step_handler(message, teach_pas)
    except ValueError:
        bot.reply_to(message.from_user.id, 'Parol noto`g`ri qaytadan kiriting !')
        bot.register_next_step_handler(message, teach_pas)


# o`qituvchi kiritadigan test nomeri
def t_num(message):
    global number_test
    try:
        if message.text.isalpha():
            number_test = message.text
        bot.send_message(message.from_user.id, 'Javob kalitlaringizni kiriting ')
        bot.send_message(message.from_user.id, '1a2b3c4d...    ')
        bot.send_message(message.from_user.id, 'Ko`rinishda')
        bot.register_next_step_handler(message, teach_ans)
    except:
        bot.send_message(message, 'Xatolik iltimos test nomerini qaytadan kiriting')
        bot.register_next_step_handler(message, t_num)


def teach_ans(message):
    global info
    data_base[number_test] = message.text
    info = 'Test nomeri :' + str(number_test) + ' ' + 'Javoblar :' + message.text
    bot.send_message(message, info)
    bot.send_message(message.from_chat.id, 'Xatolik iltimos test nomerini qaytadan kiriting')
    bot.register_next_step_handler(message, teach_ans)



bot.polling()