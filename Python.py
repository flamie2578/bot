
import telebot 
import pyowm

owm = pyowm.OWM('92db96166090b594b9cabe79fc540697')
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Portuguese
owm = OWM('92db96166090b594b9cabe79fc540697', config_dict)





bot = telebot.TeleBot("1524283639:AAGkT1mcgdg8wvW9VPrHchNMsHm5_mbYG6M")

@bot.message_handler(content_types=["text"])
def send_echo(message):
	observation = owm.weather_manager().weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')['temp']
	answer = f'Погодка: {w.detailed_status}\n'
	answer += f'Температурка: {temp}'"\n"
	
	if temp > +20:
		answer += f"А может погулять сходишь??? На улице хорошо мать твою!"
	
	elif temp > -20:
		answer += f"Обстановка так себе, что делать будешь?"
	


	bot.send_message(message.chat.id, answer)
	
bot.polling( none_stop = True)
