import telebot
from telebot import types

bot = telebot.TeleBot("1160263369:AAHKmOAGPSqSz1B0N2idYT-Okw6Q3io1UI0")
answer_teach = []
number_test = ['1']
teach_name= []
info = ''
teach_p = [12345]


answer_st = []
number_st = []
name_st = []


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
btn1 = types.KeyboardButton('O`qituvchi')
btn2 = types.KeyboardButton('Abitruyent')
markup.add(btn1,btn2)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Salom foydalanuvchi kim ekanligingizni tanlang ', reply_markup = markup )
    


@bot.message_handler(func = lambda m:True)
def echo_all(message):
    if message.text == 'O`qituvchi':
        bot.reply_to(message, 'Iltimos parolni kiriting ')
        bot.register_next_step_handler(message, teach_pas)
    elif message.text == 'Abitruyent':
        bot.reply_to(message, 'Iltimos ismingizni kiriting')
        bot.register_next_step_handler(message, name_student)
    
def teach_pas(message):
    if (str(message.text) in teach_p) == True:
        bot.reply_to(message, 'Parol to`g`ri Ismingizni kiriting')
        bot.register_next_step_handler(message, teach_na)
    else:
        bot.reply_to(message, 'Parol noto`g`ri qaytadan kiriting !')
        bot.register_next_step_handler(message, echo_all)



def teach_na (message):
    global teach_name
    teach_name = message.text.lower()
    bot.send_message(message.from_user.id, 'Test nomeri')
    bot.register_next_step_handler(message, number_test1)
    
def number_test1 (message):
    global number_test
    number_test.append(int(message.text))
    bot.send_message(message.from_user.id, 'Test kalitini yuboring')
    bot.register_next_step_handler(message, answer_teach1)

def answer_teach1(message):
    global answer_teach, info
    answer_teach = message.text.lower()
    
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text = 'Ha', callback_data = 'yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text = 'Yo`q', callback_data = 'no')
    keyboard.add(key_no)
    info = 'O`qituvchi  : ' + str(teach_name) + '  Test nomeri  : ' + str(number_test) + ' ' + ' Javoblar  : ' + str(answer_teach)
    bot.send_message(message.from_user.id, text = info, reply_markup = keyboard)


@bot.callback_query_handler(func=lambda call : True)
def calback_work(call):
    if call.data == 'yes':
       bot.send_message(call.message.chat.id, 'Ma`lumotlar muoffiaqatli jo`natildi !!!')
    elif call.data == 'no':
       bot.send_message(call.message.chat.id, 'Ma`lumotlarni qayta jo`nating ?')
       bot.reply_to(call.message, 'Iltimos ismingizni kiriting')
       bot.register_next_step_handler(call.message, teach_na, reply_markup = markup)

#talaba uchun ma`lumotlar

def name_student(message):
    global name_st
    name_st = message.text
    bot.send_message(message.from_user.id, 'Test nomeri kiriting: ')
    bot.register_next_step_handler(message, answer_aut)

def answer_aut(message):
    if (int(message.text) in number_test) == True:
        bot.register_next_step_handler(message, answer_student)
    elif (int(message.text) in number_test) == False:
        #bot.send_message(message.from_user.id, 'Test nomeri xato kiritildi iltimos tekshirib qaytadan kiriting !')
        bot.register_next_step_handler(message, name_student)

def answer_student(message):
    global answer_st
    answer_st == message.text
    bot.sen_message(message.from_user.chat.id, 'Kalitlaringizni jo`nating')



bot.polling()