import telebot
#from telebot import types

bot = telebot.TeleBot("1160263369:AAHKmOAGPSqSz1B0N2idYT-Okw6Q3io1UI0")
data_base = {
    1:'1a2b3c4d5c6d7a8d9b10a11d12c13d14c15a16a17d18b19b20a21c22d23b24d25a26d27b28c29a30c',
    2:'1a2b3a4d5c6d7a8d9b10c11d12c13a14c15d16a17b18b19b20b21c22d23b24d25a26d27b28c29a30c'

}
test_num = 0

@bot.message_handler(commands=['start'], content_types='text')
def send_welcome(message):
    bot.send_message(message, 'Kalitni yuboring :')
    bot.register_next_step_handler(message, t_num)

def t_num(message):
    test_num == int(message)
    for keys in data_base:
        if keys == test_num:
            bot.clear_reply_handlers_by_message_id(message)

