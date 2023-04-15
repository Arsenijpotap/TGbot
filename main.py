import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config
language = get_default_config()
language['language'] = 'ru'
owm = OWM('81fa964a-c8ec-4049-9e3e-1792ba1edebb', language)

bot = telebot.TeleBot('5820951961:AAHPNgrfEvQ-mHlnR74p3YkkpEheUL7W1Vo')
keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('найти контент по актеру', 'найти актеров по контенту', 'список избранного', 'завершить')
keybord2 = telebot.types.ReplyKeyboardMarkup(True)
keybord2.row('включить уведомления', 'выключить уведомления', 'обратно')
@bot.message_handler(commands=['start'])
def start_message(message):
   bot.send_message(message.chat.id, 'Здравствуйте, в моем боте вы можете найти необходимый фильм, сериал или актера.\n Также можете добавлять контент в избранное и получать уведомления по необходимой информации',reply_markup=keybord1)
@bot.message_handler(content_types=['text'])
def start_message1(message):
   if message.text=='найти актеров по контенту':
      bot.send_message(message.chat.id,'хорошо, введите название контента')
 #     @bot.message_handler(content_types=['text'])
 #     def start_message1(message):



   elif message.text=='найти контент по актеру':
      bot.send_message(message.chat.id,'хорошо, введите имя и фамилию актера')



   elif message.text=='список избранного':
      bot.send_message(message.chat.id,'хорошо', reply_markup=keybord2)
      @bot.message_handler(content_types=['text'])
      def start_message3(message1):
         if message1.text=='обратно':
            bot.send_message(message1.chat.id, 'хорошо', reply_markup=keybord1)
   elif message.text=='завершить':
      bot.send_message(message.chat.id,'до встречи')


1234567890













bot.polling()

