import telebot
from telebot import types

bot = telebot.TeleBot("1160263369:AAHKmOAGPSqSz1B0N2idYT-Okw6Q3io1UI0")
# Info O`qituvchi

answer_teach = []
number_test = 0
teach_name= []
info = ''
data_base = {}


# Info Abitruyent
answer_st = []
number_st = []
name_st = []


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
btn1 = types.KeyboardButton('O`qituvchi')
btn2 = types.KeyboardButton('Abitruyent')
markup.add(btn1,btn2)


try :
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.from_user.id, 'Salom foydalanuvchi kim ekanligingizni tanlang ', reply_markup = markup )
    

    @bot.message_handler(func = lambda m:True)
    def echo_all(message):
        if message.text == 'O`qituvchi':
            bot.reply_to(message, 'Iltimos parolni kiriting ')
            bot.register_next_step_handler(message, teach_pas)




#     O`qituvchining paroli
    def teach_pas(message):
        try:
            if int(message.text) == 12345:
                bot.reply_to(message, 'Parol to`g`ri Ismingizni kiriting')
                bot.register_next_step_handler(message, teach_na)
    
        except :
            bot.reply_to(message, 'Parol noto`g`ri qaytadan kiriting !')
            bot.register_next_step_handler(message, teach_pas)

# O`qituvchining ismi kiritiladi
    def teach_na (message):
        global teach_name
        teach_name = message.text.lower()
        bot.send_message(message.from_user.id, 'Test nomeri')
        bot.register_next_step_handler(message, number_test1)

#O`qituvchi test nomeri kiritiladi
    def number_test1 (message):
        global number_test
        number_test = int(message.text)
        bot.send_message(message.from_user.id, 'Test kalitini yuboring')
        bot.register_next_step_handler(message, answer_teach1)


# O`qituvchining javobi
    def answer_teach1(message):
        global answer_teach, data_base
        answer_teach = message.text.lower()
        data_base[teach_name] = dict()
        data_base[teach_name][number_test] = answer_teach
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text = 'Ha', callback_data = 'yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text = 'Yo`q', callback_data = 'no')
        keyboard.add(key_no)
        info = 'O`qituvchi  : ' + str(teach_name) + '  Test nomeri  : ' + str(number_test) + ' ' + ' Javoblar  : ' + str(answer_teach)
        bot.send_message(message.from_user.id, text = info, reply_markup = keyboard)
    

#Callback knopka funksiyasi
    @bot.callback_query_handler(func=lambda call : True)
    def calback_work(call):
        if call.data == 'yes':
            db_c = data_base.copy()
            for keys in data_base.keys():
                if teach_name == data_base.keys():
                    db_c[teach_name][number_test] = answer_teach
                else:
                    db_c[teach_name] = dict()
                    db_c[teach_name][number_test] = answer_teach
                data_base.clear()
                data_base = db_c.copy()
                bot.send_message(call.message.chat.id, 'Ma`lumotlar muoffiaqatli jo`natildi !!!')
        
        elif call.data == 'no':
            bot.send_message(call.message.chat.id, 'Ma`lumotlarni qayta jo`nating ?')
            bot.register_next_step_handler(call.message.chat.id, echo_all)

except:
    global message
    bot.send_message(message, 'Ma`lumotlarni jo`natishda xatolik yuz berdi ')
    bot.register_next_step_handler(message.from_chat.id, send_welcome)


bot.polling()        