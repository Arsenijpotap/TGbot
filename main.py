import telebot
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
from bs4 import BeautifulSoup
import chromedriver_binary
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
from selenium.webdriver.common.by import By
from  bs4 import *






@bot.message_handler(commands=['start'])
def start_message(message):
   bot.send_message(message.chat.id,'что вы хотите сделать?',reply_markup=keybord1 )

@bot.message_handler(content_types=['text'])
def start_message1(message):
   if message.text=='найти актеров по контенту':
      bot.send_message(message.chat.id,'хорошо, введите название контента')
      @bot.message_handler(content_types=['text'])
      def start_message123(message):
         print(message.text)


         browser = webdriver.Chrome()
         browser.get("https://www.kinopoisk.ru/?utm_referrer=yandex.by")
         search = browser.find_element(By.NAME, 'kp_query')  # search element by name
         search.send_keys('message')  # enter prompt in the search field
         find = browser.find_element(By.CSS_SELECTOR,
                                     '#__next > div.styles_root__nRLZC > div.styles_root__BJH2_.styles_headerContainer__f7XqC > header > div > div.styles_mainContainer__faOVn.styles_hasSidebar__rU_E2 > div.styles_searchFormContainerWide__3taA3.styles_searchFormContainer__GyAL5 > div > form > div > div > button > svg')  # search element by css selector
         find.click()
         find2 = browser.find_element(By.CSS_SELECTOR,
                                      '#block_left_pad > div > div:nth-child(4) > p.header > a')  # search element by css selector
         find2.click()
         find3 = browser.find_element(By.CSS_SELECTOR,
                                      '#block_left_pad > div > div.search_results.search_results_last > div:nth-child(4) > div.right > ul > li:nth-child(1) > a')  # search element by css selector
         find3.click()

         soup = BeautifulSoup(browser.page_source, 'html.parser')
         series = soup.find_all('div', class_='actorInfo')
         print(series)









   elif message.text=='найти контент по актеру':
      bot.send_message(message.chat.id,'хорошо, введите имя и фамилию актера')




   elif message.text=='список избранного':
      bot.send_message(message.chat.id,'хорошо', reply_markup=keybord2)
   elif message.text=='завершить':
      bot.send_message(message.chat.id,'до встречи')
   elif message.text=='обратно':
            bot.send_message(message.chat.id,'хорошо', reply_markup=keybord1)
            start_message(message)














bot.polling()

