# -*- coding: utf-8 -*-

import config
import telebot
import time


#mine_id = 90753007
#id[1] = 315974254
#varya_id = ""

id = [90753007, 315974254]
bot = telebot.TeleBot(config.token)

#@bot.message_handler(commands=['game'])
#def game(message):

@bot.message_handler(regexp="пересыл")
def check_answer(message):
    bot.send_message(id[0], message.text[8:])

@bot.message_handler(regexp="триггер_1")
def check_answer(message):
    bot.send_message(id[0], "Твой парень у нас. Не спрашивай как мы тебя нашли и как у тебя появился Telegram.")
    bot.send_message(id[1], "Твой парень у нас. Не спрашивай как мы тебя нашли и как у тебя появился Telegram.")
    time.sleep(3)
    bot.send_message(id[0], "Время - деньги. Так что не задавай лишних вопросов и делай то что тебе говорят.")
    bot.send_message(id[1], "Время - деньги. Так что не задавай лишних вопросов и делай то что тебе говорят.")
    time.sleep(3)
    bot.send_message(id[0], "Вот первое задание:")
    bot.send_message(id[1], "Вот первое задание:")
    time.sleep(1)
    bot.send_message(id[0], "Найди место где время искажено *я пока хуй его как это сюда подвязать*")
    bot.send_message(id[1], "Найди место где время искажено *я пока хуй его как это сюда подвязать*")
    time.sleep(2)
    bot.send_message(id[0], "Тебе придётся заморать руки. Найди код и пришли его нам. Часики тикают.")
    bot.send_message(id[1], "Тебе придётся заморать руки. Найди код и пришли его нам. Часики тикают.(код тьма)")
    time.sleep(3)
    bot.send_message(id[0], "Если тебе нужна подсказка, просто спроси ``подсказка и номер вопроса``.")
    bot.send_message(id[1], "Если тебе нужна подсказка, просто спроси ``подсказка и номер вопроса``.")

@bot.message_handler(regexp="тьма|Тьма")
def check_answer(message):
    bot.send_message(id[0], "Отлично. Ты справилась с первым заданием.")
    bot.send_message(id[1], "Отлично. Ты справилась с первым заданием.")
    time.sleep(3)
    bot.send_message(id[0], "Но что-то ты очень долго. Наши парни проголодались - тебе придётся раздобыть для них пищу.")
    bot.send_message(id[1], "Но что-то ты очень долго. Наши парни проголодались - тебе придётся раздобыть для них пищу.")
    time.sleep(3)
    bot.send_message(id[0], "Мы слышали, недалеко от тебя есть место где продаётся очень вкусная еда")
    bot.send_message(id[1], "Мы слышали, недалеко от тебя есть место где продаётся очень вкусная еда")
    time.sleep(1)
    bot.send_message(id[0], "Мы обо всём договоримся. Тебе лишь надо сказать кодовое слово - Клин")
    bot.send_message(id[1], "Мы обо всём договоримся. Тебе лишь надо сказать кодовое слово - Клин")
    time.sleep(2)
    bot.send_message(id[0], "Поторопись.")
    bot.send_message(id[1], "Поторопись.")

@bot.message_handler(regexp="овод|Овод")
def check_answer(message):
    bot.send_message(id[0], "Я уже чую запах. Тебе нужно доставить её в места не столь отдаленные.")
    bot.send_message(id[1], "Я уже чую запах. Тебе нужно доставить её в места не столь отдаленные.")
    time.sleep(3)
    bot.send_message(id[0], "Найди место где очень много наших ребят.")
    bot.send_message(id[1], "Найди место где очень много наших ребят.")
    time.sleep(3)
    bot.send_message(id[0], "Ты легко их узнаешь. У них красные глаза, они мало спят и сходят с ума при виде всяких каракуль")
    bot.send_message(id[1], "Ты легко их узнаешь. У них красные глаза, они мало спят и сходят с ума при виде всяких каракуль")
    time.sleep(1)
    bot.send_message(id[0], "Ступай. Не теряй времени.")
    bot.send_message(id[1], "Ступай. Не теряй времени.")
    time.sleep(2)
    bot.send_message(id[0], "И да, если хочешь можешь укусить шаурму. Так уж и быть, мы не такие жестокие")
    bot.send_message(id[1], "И да, если хочешь можешь укусить шаурму. Так уж и быть, мы не такие жестокие")
    
@bot.message_handler(regexp="йопта|Йопта")
def check_answer(message):
    bot.send_message(id[0], "Да ты не промах. И с этим справилась.")
    bot.send_message(id[1], "Да ты не промах. И с этим справилась.")
    time.sleep(3)
    bot.send_message(id[0], "Осталось последнее задание и мы вернем тебе парня.")
    bot.send_message(id[1], "Осталось последнее задаине и мы вернем тебе парня.")
    time.sleep(3)
    bot.send_message(id[0], "В такой знаменательный день хочется всё сгладить бутылочкой холодненького Фрау Марта.")
    bot.send_message(id[1], "В такой знаменательный день хочется всё сгладить бутылочкой холодненького Фрау Марта.")
    time.sleep(1)
    bot.send_message(id[0], "Ты знаешь где его найти.")
    bot.send_message(id[1], "Ты знаешь где его найти.")
    time.sleep(2)
    bot.send_message(id[0], "Мы обо всём договоримся. Тебе лишь нужно сказать - Курлык курлык")
    bot.send_message(id[1], "Мы обо всём договоримся. Тебе лишь нужно сказать - Курлык курлык")

@bot.message_handler(regexp="пивас|Пивас")
def check_answer(message):
    bot.send_message(id[0], "Отлично. Последний шаг - принеси его нашему человеку.")
    bot.send_message(id[1], "Отлично. Последний шаг - принеси его нашему человеку.")
    time.sleep(3)
    bot.send_message(id[0], "Недалеко от тебя есть общежития. Иди туда.")
    bot.send_message(id[1], "Недалеко от тебя есть общежития. Иди туда.")


@bot.message_handler(regexp="подсказка 1")
def check_answer(message):
    bot.send_message(id[0], "Подсказка 1")
    bot.send_message(id[1], "Подсказка 1")

@bot.message_handler(regexp="подсказка 2")
def check_answer(message):
    bot.send_message(id[0], "Подсказка 2")
    bot.send_message(id[1], "Подсказка 2")

@bot.message_handler(regexp="подсказка 3")
def check_answer(message):
    bot.send_message(id[0], "Подсказка 3")
    bot.send_message(id[1], "Подсказка 3")

@bot.message_handler(content_types=['text'])
def check_answer(message):
    bot.send_message(id[0], "Хач мне прислал: " + message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)