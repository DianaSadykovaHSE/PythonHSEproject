import telebot
from telebot import types
bot = telebot.TeleBot(token='6425808976:AAGc8YCpgX_HXpnZykzCZTGGsOMXTtG5l7Q')

@bot.message_handler(commands=['start'])
def corpus(message):
    '''принимает на вход команду начала работы с ботом, выводит кнопки с выбором корпуса в панеле ввода сообщения'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Pokra = types.KeyboardButton('Покровка', )
    Vavilova = types.KeyboardButton('Вавилова, 7')
    markup.add(Pokra, Vavilova)
    bot.send_message(message.chat.id, 'Привет, выбери свой <b>корпус</b>!', parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def place(message):
    '''обработчик текстовых сообщений
    на каждое сообщение выводит кнопки для выбора локации'''
    #предлагает пользователю выбрать место на Покровке
    if message.text == 'Покровка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        P_Stol = types.KeyboardButton('Столовая на Покровке')
        P_Gar = types.KeyboardButton('Гардероб на Покровке')
        P_Tual = types.KeyboardButton('Библиотека/читальный зал на Покровке')
        markup.add(P_Stol, P_Gar, P_Tual)
        bot.send_message(message.chat.id, 'Выбери место, которое тебе нужно найти', parse_mode='html', reply_markup=markup)

    #предлагает пользователю выбрать место на Вавилова, 7
    elif message.text == 'Вавилова, 7':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Vav_Stol = types.KeyboardButton('Столовая на Вавилова, 7')
        Vav_Gar = types.KeyboardButton('Гардероб на Вавилова, 7')
        Vav_Tual = types.KeyboardButton('Библиотека/читальный зал на Вавилова, 7')
        markup.add(Vav_Stol, Vav_Gar, Vav_Tual)
        bot.send_message(message.chat.id, 'Выбери место, которое тебе нужно найти', parse_mode='html', reply_markup=markup)

    #рассказывает пользователю о столовых и кофейнях на Покровке
    elif message.text=='Столовая на Покровке':
        a = "Jeffrey's"
        markup_1 = types.InlineKeyboardMarkup()
        markup_1.add(types.InlineKeyboardButton('Посмотреть меню', url='www.grusha.cafe'))
        markup_2 = types.InlineKeyboardMarkup()
        markup_2.add(types.InlineKeyboardButton('Посмотреть меню', url='www.jeffreys.ru'))
        bot.send_message(message.chat.id, '<b>Большая столовая</b> расположена на 1 этаже корпусе N, её будет видно при выходе из центрального атриума по направлению к корпусам M, N, R, S', parse_mode='html')
        bot.send_message(message.chat.id, '<b>Кофейня</b> расположена на 1 этаже корпусе F, её будет видно при выходе из центрального атриума по направлению к корпусам F, D, G', parse_mode='html')
        bot.send_message(message.chat.id, '<b>Кофейня "Груша"</b> расположена на 1 этаже в корпусе S, её будет видно при входе в корпус R с улицы или можно пройти от центрального атриума: пойти по направлению к корпусам M, N, R, S, повернуть направо и в конце коридора по правую сторону от тебя будет кофейня', parse_mode='html', reply_markup=markup_1)
        bot.send_message(message.chat.id, f'<b>Кофейня {a}</b> расположена на -1 этаже в корпусе S, в нее можно пройти от центрального атриума: пойти по направлению к корпусам M, N, R, S, повернуть направо и в середине коридора по правую сторону увидишь лестницу, спустившись по которой, ты придёшь в кофейню', parse_mode='html', reply_markup=markup_2)
        Itog_n = types.InlineKeyboardMarkup()
        Itog_n.add(types.InlineKeyboardButton('Нет, оценить работу бота', callback_data='mark'), types.InlineKeyboardButton('Да, вернуться в начало', callback_data='return'))
        bot.send_message(message.chat.id, 'У тебя остались вопросы?',  reply_markup=Itog_n)

    #рассказывает пользователю о гардеробах на Покровке
    elif message.text=='Гардероб на Покровке':
        bot.send_message(message.chat.id,'<b>Первый гардероб (без номерков)</b> расположен на 1 этаже корпусе D, на первом этаже (проходим через турникет и спускаемся вниз по лестнице), он будет удобен для тех, кто идет с Покровского бульвара', parse_mode='html')
        bot.send_message(message.chat.id,'<b>Второй гардероб (с номерками)</b> расположен на 1 этаже корпусе R, его будет видно при входе со стороны корпуса R, он будет удобен для тех, кто идет с улицы Воронцово Поле', parse_mode='html')
        Itog_n = types.InlineKeyboardMarkup()
        Itog_n.add(types.InlineKeyboardButton('Нет, оценить работу бота', callback_data='mark'),
                   types.InlineKeyboardButton('Да, вернуться в начало', callback_data='return'))
        bot.send_message(message.chat.id, 'У тебя остались вопросы?', reply_markup=Itog_n)

    #рассказывает пользователю о библиотеках на Покровке
    elif message.text=='Библиотека/читальный зал на Покровке':
        bot.send_message(message.chat.id,'<b>Самая большая библиотека-читальный зал в Вышке</b> расположена на 2 этаже корпусе N над столовой, её будет видно при выходе из центрального атриума по направлению к корпусам M, N, R, S', parse_mode='html')
        bot.send_message(message.chat.id,'<b>Также библиотеки есть в корпусах R (2 этаж, аудитория R210-214, R216-217) и S (1 этаж)</b> ', parse_mode='html')
        Itog_n = types.InlineKeyboardMarkup()
        Itog_n.add(types.InlineKeyboardButton('Нет, оценить работу бота', callback_data='mark'),
                   types.InlineKeyboardButton('Да, вернуться в начало', callback_data='return'))
        bot.send_message(message.chat.id, 'У тебя остались вопросы?', reply_markup=Itog_n)

    #рассказывает пользователю о столовой-буфете на Вавилова, 7
    elif message.text=='Столовая на Вавилова, 7':
        bot.send_message(message.chat.id, '<b>Буфет самообслуживания</b> расположен на 10 этаже, до туда можно добраться только на лифте. В меню комплексы и снеки.', parse_mode='html')
        Itog_n = types.InlineKeyboardMarkup()
        Itog_n.add(types.InlineKeyboardButton('Нет, оценить работу бота', callback_data='mark'),
                   types.InlineKeyboardButton('Да, вернуться в начало', callback_data='return'))
        bot.send_message(message.chat.id, 'У тебя остались вопросы?', reply_markup=Itog_n)

    #рассказывает пользователю о гарберобе на Вавилова, 7
    elif message.text=='Гардероб на Вавилова, 7':
        bot.send_message(message.chat.id, '<b>Гардероб (без номерков)</b> расположен на 2 этаже (комната 219), выходим из лифта, дважды поворачиваем налево (гардероб будет по левую сторону)', parse_mode='html')
        Itog_n = types.InlineKeyboardMarkup()
        Itog_n.add(types.InlineKeyboardButton('Нет, оценить работу бота', callback_data='mark'),
                   types.InlineKeyboardButton('Да, вернуться в начало', callback_data='return'))
        bot.send_message(message.chat.id, 'У тебя остались вопросы?', reply_markup=Itog_n)

    #рассказывает пользователю о библиотеке на Вавилова, 7
    elif message.text=='Библиотека/читальный зал на Вавилова, 7':
        bot.send_message(message.chat.id, '<b>Библиотеки</b> в корпусе нет, но небольшая коллекция книг находится в комнате 213 (в конце аудитории на стеллажах). Чтобы найти 213 комнату, нужно выйти из лифта, дважды повернуть налево (она будет по правую сторону).', parse_mode='html')
        Itog_n = types.InlineKeyboardMarkup()
        Itog_n.add(types.InlineKeyboardButton('Нет, оценить работу бота', callback_data='mark'),
                   types.InlineKeyboardButton('Да, вернуться в начало', callback_data='return'))
        bot.send_message(message.chat.id, 'У тебя остались вопросы?', reply_markup=Itog_n)

@bot.callback_query_handler(func=lambda call: call.data == 'return')
def marking(call):
    '''принимает запрос при нажатии кнопки 'Да,вернуться в начало' и выводит кнопки с выбором корпуса в панеле ввода сообщения'''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Pokra = types.KeyboardButton('Покровка')
    Vavilova = types.KeyboardButton('Вавилова, 7')
    markup.add(Pokra, Vavilova)
    bot.send_message(call.message.chat.id, 'Привет, выбери свой <b>корпус</b>!', parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'mark')
def marking(call):
    '''принимает запрос при нажатии кнопки 'нет, оценить бота' и выводит кнопки с оценками от 1 до 5'''
    Itog_m = types.InlineKeyboardMarkup()
    Itog_m.add(types.InlineKeyboardButton('1', callback_data='num_1'),
               types.InlineKeyboardButton('2', callback_data='num_2'),
               types.InlineKeyboardButton('3', callback_data='num_3'),
               types.InlineKeyboardButton('4', callback_data='num_4'),
               types.InlineKeyboardButton('5', callback_data='num_5'))
    bot.send_message(call.message.chat.id, 'Выберете оценку от 1 до 5, где 5 - очень понравилось, 1 - не понравилось совсем', reply_markup=Itog_m)

@bot.callback_query_handler(func=lambda call: True if call.data in['num_1', 'num_2', 'num_3', 'num_4', 'num_5'] else False)
def marking(call):
    '''принимает запрос при нажатии кнопки-цифры и записывает оценку в файл'''
    b=call.data.split('_')[1] #вытаскивает из называния функции оценку
    f = open('marks_bot', 'a')
    f.write(b) #записывает оценку в файл
    f.write('\n')
    bot.send_message(call.message.chat.id, 'Спасибо за оценку!')
    f.close()
bot.polling(non_stop=True)
