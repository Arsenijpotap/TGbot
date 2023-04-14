import telebot
bot = telebot.TeleBot('5820951961:AAHPNgrfEvQ-mHlnR74p3YkkpEheUL7W1Vo')
@bot.message_handler(commands=['start'])
def start_message(message):
   bot.send_message(message.chat.id, 'Здравствуйте, в моем боте вы можете найти необходимый фильм, сериал или актера.\n Также можете добавлять контент в избранное и получать уведомления по необходимой информации')

keyboard1 =k
bot.polling()

