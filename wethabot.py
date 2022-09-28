import os
import telebot
from dotenv import load_dotenv
load_dotenv()

#That part still doesn't work (need to find some solution)

API_KEY_TG = os.getenv('API_KEY_TG')
bot = telebot.TeleBot(API_KEY_TG)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b> Where are you from? </b>', parse_mode='html')

# @bot.message_handler()
# def get_user_text(message):



bot.polling(none_stop=True)


