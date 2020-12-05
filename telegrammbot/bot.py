import telebot
from telebot import types

bot = telebot.TeleBot("1160263369:AAHKmOAGPSqSz1B0N2idYT-Okw6Q3io1UI0")
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn1 = types.KeyboardButton('O`qituvchi')
btn2 = types.KeyboardButton('Foydalanuvchi')
btn3 = types.KeyboardButton('Baza')
markup.add(btn1, btn2, btn3)

@bot.message_handler(commands=['start'] ,content_types='text')
try:
    def send_welcome(message):
        bot.send_message(message.from_user.id, 'Salom foydalanuvchi kim aqilli botga xush kelibsiz ', reply_markup=markup)
        if message.text == 'O`qituvchi':
            bot.reply_to(message, 'Iltimos parolni kiriting ')
            bot.register_next_step_handler(message, teach_pas)
        elif message.text == 'Foydalanuvchi':
            pass
        elif message.text == 'Baza':
            bot.register_next_step_handler(message, base)
except Exception:
    pass
finally:
    send_welcome(message)
