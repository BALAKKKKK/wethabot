import os
import telebot

#That part still doesn't work (need to find some solution)
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b> Where are you from? </b>', parse_mode='html')

bot.polling(none_stop=True)


