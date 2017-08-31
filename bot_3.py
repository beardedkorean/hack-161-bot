# -*- coding: utf-8 -*-

import config
import telebot
import time


mine_id = 90753007
hach_id = 315974254
varya_id = ""

bot = telebot.TeleBot(config.token)

#@bot.message_handler(commands=['game'])
#def game(message):

@bot.message_handler(regexp="пересыл")
def check_answer(message):
    bot.send_message(mine_id, message.text[8:])

@bot.message_handler(regexp="триггер_1")
def check_answer(message):
    bot.send_message(mine_id, "Твой парень у нас. Не спрашивай как мы тебя нашли и как у тебя появился Telegram.")
    bot.send_message(hach_id, "Твой парень у нас. Не спрашивай как мы тебя нашли и как у тебя появился Telegram.")
    time.sleep(3)
    bot.send_message(mine_id, "Время - деньги. Так что не задавай лишних вопросов и делай то что тебе говорят.")
    bot.send_message(hach_id, "Время - деньги. Так что не задавай лишних вопросов и делай то что тебе говорят.")
    time.sleep(3)
    bot.send_message(mine_id, "Вот первое задание:")
    bot.send_message(hach_id, "Вот первое задание:")
    time.sleep(1)
    bot.send_message(mine_id, "Найди место где время искажено *я пока хуй его как это сюда подвязать*")
    bot.send_message(hach_id, "Найди место где время искажено *я пока хуй его как это сюда подвязать*")
    time.sleep(2)
    bot.send_message(mine_id, "Тебе придётся заморать руки. Найди код и пришли его нам. Часики тикают.")
    bot.send_message(hach_id, "Тебе придётся заморать руки. Найди код и пришли его нам. Часики тикают.(код тьма)")
    time.sleep(3)
    bot.send_message(mine_id, "Если тебе нужна подсказка, просто спроси ``подсказка и номер вопроса``.")
    bot.send_message(hach_id, "Если тебе нужна подсказка, просто спроси ``подсказка и номер вопроса``.")

@bot.message_handler(regexp="тьма|Тьма")
def check_answer(message):
    bot.send_message(mine_id, "Отлично. Ты справилась с первым заданием.")
    bot.send_message(hach_id, "Отлично. Ты справилась с первым заданием.")
    time.sleep(3)
    bot.send_message(mine_id, "Но что-то ты очень долго. Наши парни проголодались - тебе придётся раздобыть для них пищу.")
    bot.send_message(hach_id, "Но что-то ты очень долго. Наши парни проголодались - тебе придётся раздобыть для них пищу.")
    time.sleep(3)
    bot.send_message(mine_id, "Мы слышали, недалеко от тебя есть место где продаётся очень вкусная еда")
    bot.send_message(hach_id, "Мы слышали, недалеко от тебя есть место где продаётся очень вкусная еда")
    time.sleep(1)
    bot.send_message(mine_id, "Мы обо всём договоримся. Тебе лишь надо сказать кодовое слово - Клин")
    bot.send_message(hach_id, "Мы обо всём договоримся. Тебе лишь надо сказать кодовое слово - Клин")
    time.sleep(2)
    bot.send_message(mine_id, "Поторопись.")
    bot.send_message(hach_id, "Поторопись.")


@bot.message_handler(regexp="подсказка 1")
def check_answer(message):
    bot.send_message(mine_id, "Подсказка 1")
    bot.send_message(hach_id, "Подсказка 1")

@bot.message_handler(regexp="подсказка 2")
def check_answer(message):
    bot.send_message(mine_id, "Подсказка 2")
    bot.send_message(hach_id, "Подсказка 2")

@bot.message_handler(regexp="подсказка 3")
def check_answer(message):
    bot.send_message(mine_id, "Подсказка 3")
    bot.send_message(hach_id, "Подсказка 3")

@bot.message_handler(content_types=['text'])
def check_answer(message):
    bot.send_message(mine_id, "Хач мне прислал" + message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)