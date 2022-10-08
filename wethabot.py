import requests
import os
import telebot
from dotenv import load_dotenv
load_dotenv()

# Key information
API_KEY_TG = os.getenv('API_KEY_TG')
bot = telebot.TeleBot(API_KEY_TG)
base_url = "http://api.openweathermap.org/data/2.5/weather?"
ow_key = os.getenv('API_KEY_OW')

# Select the convenient emoji depending on the weather
def emoji_checker(description): 
    description = str(description)
    atmosphere = {'mist', 'smoke', 'haze', 'fog', 'sand', 'dust', 'volcanic ash', 'squalls', 'tornado'}
    if 'cloud' in description:
        return '\u2601'
    elif atmosphere.intersection(set(description.split())):
        return '\U0001F32B'
    elif 'clear sky' in description:
        return '\u2600'
    elif 'rain' in description or 'drizzle' in description or 'thunderstorm' in description:
        return '\u2614'
    elif 'snow' in description or 'sleet' in description:
        return '\u2744'
    else:
        return '\u2753'


# Introduce message
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b> Where are you from? </b>', parse_mode='html')



# Weather answer
@bot.message_handler()
def get_user_text(message):

    city_name = message.text
    full_city_url = base_url + "appid=" + ow_key + '&q=' + city_name
    response = requests.get(full_city_url)
    x = response.json()


    if x["cod"] != "404":
        y = x["main"]
        z = x["weather"]
        weather_description = z[0]["description"]
        emoji = emoji_checker(weather_description)
        weather_description = weather_description[0].upper() + weather_description[1:].lower()
        current_temperature = '<b>' + str(int(round(float(y["temp"]) - 273.15))) + ' °C' + '</b>'
        temp = current_temperature + ' - ' + weather_description + emoji

    else:
        temp = 'City not found'


    bot.send_message(message.chat.id, temp, parse_mode='html')



bot.polling(none_stop=True)

