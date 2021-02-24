import telebot

bot = telebot.TeleBot('1672695744:AAHRjByoDREPlrc9YeUcXFHuHrjcxjTDpHo') #ключ бота

#работа с клавишами
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Контакты', 'Устав ТСН', 'Схема ТСН')
keyboard1.row('Смета ТСН', 'Членские взносы', 'Целевые взносы')
keyboard1.row('Реквизиты оплаты', 'Аварийная')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Смета 2020', 'Смета 2021')
keyboard2.row('Назад')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('Целевой взнос 2020', 'Целевой взнос 2021')
keyboard3.row('Назад')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row('Членский взнос 2020', 'Членский взнос 2021')
keyboard4.row('Назад')
#закончили клавиши

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Данный бот, создан для получения актуальной информации о поселке ТСН "Нижний Хутор"', reply_markup=keyboard1)
#работа с командами
@bot.message_handler(content_types=['text','photo', 'document'])
def send_text(message):
    if message.text.lower() == 'контакты':
        bot.send_message(message.chat.id,
'Контакты правления:                      Председатель:                                      Cергей Васильевич Колесник                 Тел.: +7-931-253-43-56                    Эл.почта: infohutor@mail.ru                   Общие вопросы, вопросы по оплате и начислению взносов, оплате воды и электричества.                                               Член правления:                                                         Владимир Васильевич Козлов                         Тел.: +7-981-893-59-92                                        Ответственный за водоснабжение, опломбирование счетчиков на воду.    Член правления:                                Леонид Николаевич Чубарь                            Тел.: +7-911-911-66-64                                      Ответственный за доступ к воротам на въезде в поселок.')
    elif message.text.lower() == 'реквизиты оплаты':
        bot.send_message(message.chat.id, 'Реквизиты для оплаты на счет ТСН «Нижний Хутор»                                               1) При оплате членского взноса в назначении платежа указывается: «Членский взнос, ФИО, месяц оплаты, и последние цифры кадастрового номера участка» Кадастровый номер: 47:14:0501006:81                                        Пример: Членский взнос, Петров Иван Иванович, январь, 81                                         2) При оплате воды в назначении платежа указывается: «Оплата ХВС, текущие показания прибора учета воды, ФИО, месяц и последние цифры кадастрового номера участка»                                    Пример: Оплата ХСВ, 151, Петров Иван Иванович, январь, 81.                                Стоимость воды на январь 2021г: 67,05 руб.- 1 куб.метр.                                                          3) При оплате электричества (для тех, кто еще не перешел на индивидуальные счетчики!!!) в назначении платежа указывается: «Оплата, текущие показания приборов учета электроэнергии, ФИО, месяц и последние цифры кадастрового номера участка»                                                    Пример: Оплата электричества, Т1 3333, Т2 2222, Петров Иван Иванович, январь, 81                                                                          Стоимость электроэнергии:                               Т1- 5,18 руб. ; Т2- 2,81 руб.                                                    Реквизиты ТСН «Нижний хутор» р/сч 40703810932180000087, к/сч 30101810600000000786, ИНН: 472500150 КПП: 472501001 Банк: ФИЛИАЛ «САНКТ-ПЕТЕРБУРГСКИЙ» АО «АЛЬФА-БАНК» БИК: 044030786')
    elif message.text.lower() == 'аварийная':
        bot.send_message(message.chat.id,'В случае отключения электроэнергии звонить по номеру 8 (800) 220-02-20. Могут спросить номер трансформатора - ТП 2318')

    elif message.text.lower() == 'членский взнос 2020':
        bot.send_message(message.chat.id,'Членский взнос 9 545 рублей в год')

    elif message.text.lower() == 'смета тсн':
        bot.send_message(message.chat.id,'Смета ТСН', reply_markup=keyboard2)

    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id,'Главное меню', reply_markup=keyboard1)

    elif message.text.lower() == 'целевые взносы':
        bot.send_message(message.chat.id,'Целевые взносы', reply_markup=keyboard3)

    elif message.text.lower() == 'членские взносы':
        bot.send_message(message.chat.id,'Членские взносы', reply_markup=keyboard4)

    elif message.text.lower() == 'целевой взнос 2020':
        bot.send_message(message.chat.id,'Ошибка 404. Мы уже работаем над исправлением😉')
    elif message.text.lower() == 'смета 2020':
        bot.send_photo(message.chat.id, open("smeta2020.jpg", "rb"))
    elif message.text.lower() == 'схема тсн':
        bot.send_photo(message.chat.id, open("shema.jpg", "rb"))
    elif message.text.lower() == 'устав тсн':
        bot.send_document(message.chat.id, open("ustav.pdf", "rb"))
    elif message.text.lower() == 'членский взнос 2021':
        bot.send_message(message.chat.id,'В разработке....')
    elif message.text.lower() == 'целевой взнос 2021':
        bot.send_message(message.chat.id,'В разработке....')
    elif message.text.lower() == 'смета 2021':
        bot.send_message(message.chat.id,'В разработке....')    
        #окончание команд

bot.polling()
