import telebot
from telebot import types

bot = telebot.TeleBot("1160263369:AAHKmOAGPSqSz1B0N2idYT-Okw6Q3io1UI0")


data_base = {
    1:'1a2a3a',
    2:'1b2b3b',
    3:'1c2c3c'
}
global b
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn1 = types.KeyboardButton('O`qituvchi')
btn2 = types.KeyboardButton('Foydalanuvchi')
btn3 = types.KeyboardButton('Baza')

markup.add(btn1, btn2, btn3)
try:
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.from_user.id, 'Salom foydalanuvchi kim aqilli botga xush kelibsiz ', reply_markup=markup)

    @bot.message_handler(content_types='text')
    def begin_bot(message):
        if message.text == 'O`qituvchi':
            bot.reply_to(message, 'Iltimos parolni kiriting ')
            bot.register_next_step_handler(message, teach_pas)
        elif message.text == 'Foydalanuvchi':
            pass
        elif message.text == 'Baza':
            bot.register_next_step_handler(message, base)
except Exception:
    pass
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

def t_num(message):
    global number_test
    try:
        if message.text.isdigit():
            number_test = int(message.text)
            bot.send_message(message.from_user.id, 'Javob kalitlaringizni kiriting ')
            bot.send_message(message.from_user.id, '1a2b3c4d...    ')
            bot.send_message(message.from_user.id, 'Ko`rinishda')
            bot.register_next_step_handler(message, teach_ans)

        else:
            bot.send_message(message.from_user.id, 'Iltimos son kiriting ')
            bot.register_next_step_handler(message, t_num)

    except Exception:
        bot.send_message(message, 'Xatolik iltimos test nomerini qaytadan kiriting')
        bot.register_next_step_handler(message, t_num)
    
def teach_ans(message):
    try:
        data_base[number_test] = str(message)
        bot.send_message(message, 'Ma`lumotlar jo`natildi ')
    except:
        bot.send_message(message, 'Xatolik yuz berdi ')
        bot.register_next_step_handler(message, t_num)

global a
def base(message):
    for keys in data_base:
        bot.send_message(message, keys)
        bot.send_message(message, str(data_base[keys]))




bot.polling()