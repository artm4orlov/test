import telebot
from telebot import types
bot = telebot.TeleBot("5843267228:AAEzYBurd3agiOER531vttf_pUeu8Z54sxY")
tro = 0

@bot.message_handler(commands=["play"])
def send_welcome(message):
bot.reply_to(message, "Howdy, how are you doing?")
mp = types.ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
tp1 = types.KeyboardButton("Согласен")
tp2 = types.KeyboardButton("Не согласен")
tp3 = types.KeyboardButton("Подумаю")
mp.add(tp1,tp2,tp3)
send_mess = f"<b>Зравствуй пользователь{message.from_user.first_name} {message.from_user.last_name}<b>\n Хочешь пройти тест по биологии?"
bot.send_message(message.chat.id,send_mess, parse_mode='html', reply_markup=mp)

@bot.message_handler(func=lambda m :True)
def test_begin(message):
global tro
if message.text == "Согласен":
tro +=1

mp = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
tp1 = types.KeyboardButton("в правом желудочке")
tp2 = types.KeyboardButton("в левом желудочке")
tp3 = types.KeyboardButton("в обоих желудочках")
mp.add(tp1, tp2, tp3)
bot.send_message(message.chat.id,"1.Где начинается большой круг кровообращения?", parse_mode='html', reply_markup=mp)
bot.register_next_step_handler(message, question_2)

def question_2(message):
global tro
if message.text == "Согласен":
tro +=1

mp = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
tp1 = types.KeyboardButton("кровь течет к сердцу")
tp2 = types.KeyboardButton("кровь течет от сердца")
tp3 = types.KeyboardButton("кровь течет от артерий к венам")
mp.add(tp1, tp2, tp3)
bot.send_message(message.chat.id,"2.Как течет кровь в артериях?", parse_mode='html', reply_markup=mp)
bot.register_next_step_handler(message, question_3)

def question_3(message):
global tro
if message.text == "кровь течет от сердца":
tro += 1

mp = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
tp1 = types.KeyboardButton("1группа")
tp2 = types.KeyboardButton("2 группа")
tp3 = types.KeyboardButton("3 группа ")
tp4 = types.KeyboardButton("4группа")
mp.add(tp1, tp2, tp3, tp4)
bot.send_message(message.chat.id,"3.Какая группа крови является универсальным донором?", parse_mode='html', reply_markup=mp)
bot.register_next_step_handler(message, question_4)

def question_4(message):
global tro
if message.text == "1группа":
tro += 1

mp = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
tp1 = types.KeyboardButton("в левом предсердии")
tp2 = types.KeyboardButton("в левом желудочке ")
tp3 = types.KeyboardButton("в правом предсердии")
tp4 = types.KeyboardButton("в правом желудочке")
mp.add(tp1, tp2, tp3, tp4)
bot.send_message(message.chat.id,"4.Где заканчивается малый круг кровообращения?", parse_mode='html', reply_markup=mp)
bot.register_next_step_handler(message, question_5)

def question_5(message):
global tro
if message.text == "в левом предсердии":
tro +=1

mp = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
tp1 = types.KeyboardButton("содержит готовые антитела ")
tp2 = types.KeyboardButton("препарат из убитых микробов")
mp.add(tp1, tp2)
bot.send_message(message.chat.id,"5.Что содержит вакцина?", parse_mode='html', reply_markup=mp)
bot.register_next_step_handler(message, question_6)

def question_6(message):
global tro
if message.text == "препарат из убитых микробов":
tro +=1

mp = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
tp1 = types.KeyboardButton("гипотония")
tp2 = types.KeyboardButton("гипертония")
mp.add(tp1, tp2)
bot.send_message(message.chat.id,"6.Как называется стойкое повышенное артериальное давление?", parse_mode='html', reply_markup=mp)
bot.register_next_step_handler(message, question_7)

def question_7(message):
global tro
if message.text == "гипертония":
tro +=1

mp = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
tp1 = types.KeyboardButton("инсульт")
tp2 = types.KeyboardButton("инфаркт")
mp.add(tp1, tp2)
bot.send_message(message.chat.id,"7.Кровоизлияние в мышцу сердца называется?", parse_mode='html', reply_markup=mp)
bot.register_next_step_handler(message, question_8)

def question_8(message):
global tro
if message.text == "инфаркт":
tro +=1

mp = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
tp1 = types.KeyboardButton("в стенках много мышечных эластичных элементов")
tp2 = types.KeyboardButton("в стенках мало мышечных эластичных элементов")
tp3 = types.KeyboardButton("состоят из одного слоя клеток")
mp.add(tp1, tp2, tp3)
bot.send_message(message.chat.id,"8.Особенности строения капиляр?", parse_mode='html', reply_markup=mp)
bot.register_next_step_handler(message, question_9)


def question_9(message):
global tro
if message.text == "состоят из одного слоя клеток":
tro +=1

mp = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
tp1 = types.KeyboardButton("недостаток кислорода")
tp2 = types.KeyboardButton("алкоголь")
tp2 = types.KeyboardButton("много активности")
tp4 = types.KeyboardButton("некотин")
mp.add(tp1, tp2, tp3, tp4)
bot.send_message(message.chat.id,"9.Выберите вернные ответы:"
                                 "Фауторы негативно влияющие на сердце?", parse_mode='html', reply_markup=mp)
bot.register_next_step_handler(message, question_10)


def question_10(message):
global tro
if message.text == "недостаток кислорода,алкоголь,некотин":
tro +=1

mp = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
tp1 = types.KeyboardButton("правописание")
tp2 = types.KeyboardButton("живоный и растительный мир")
tp3 = types.KeyboardButton("историю страны")
mp.add(tp1, tp2, tp3)
bot.send_message(message.chat.id,"10.Что изучает биология?", parse_mode='html', reply_markup=mp)
bot.register_next_step_handler(message, question_)








