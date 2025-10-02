import telebot
import random
import requests
from datetime import datetime

token = "your token"

stories=[
    'анекдот 1',
    'анекдот 2',
    'анекдот 3',
    'анекдот 4',
]

api = 'https://yandex.com/time/sync.json?geo=213'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def hello_message(message):
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(content_types='text')
def story(message):
    if message.text=="анекдот":
        story = stories[random.randint(0,3)]
        bot.send_message(message.chat.id, story)
    elif message.text=="время":
        time = int(requests.get(api).json()['time'])/1000
        local_datetime = datetime.fromtimestamp(time)
        bot.send_message(message.chat.id, local_datetime)

    else:
        bot.send_message(message.chat.id, "неизвестная команда")


bot.polling(none_stop=True, interval=0)