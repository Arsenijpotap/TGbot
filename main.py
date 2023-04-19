import re

import telebot
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
alf = 'йцукенгшщзхъфывапролджэячсмитьбюё'
Alf= alf.upper()
print(Alf[2])
counter = 0
a=1

s=0


@bot.message_handler(commands=['start'])
def start_message(message):
   bot.send_message(message.chat.id,'что вы хотите сделать?',reply_markup=keybord1 )
   counter = 1
@bot.message_handler(content_types=['text'])
def start_message1(message):
   if message.text=='найти актеров по контенту':
      bot.send_message(message.chat.id,'хорошо, введите название контента')
      counter=1










   elif message.text=='найти контент по актеру':
      bot.send_message(message.chat.id,'хорошо, введите имя и фамилию актера')




   elif message.text=='список избранного':
      bot.send_message(message.chat.id,'хорошо', reply_markup=keybord2)
   elif message.text=='завершить':
      bot.send_message(message.chat.id,'до встречи')
   elif message.text=='обратно':
            bot.send_message(message.chat.id,'хорошо', reply_markup=keybord1)
            start_message(message)

   elif a == 1:


    # search by film

          browser = webdriver.Chrome()
          browser.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
          search = browser.find_element(By.NAME, 'kp_query')  # search element by name
          search.send_keys(message.text)  # enter prompt in the search field
          findactor = browser.find_element(By.CSS_SELECTOR,
                                      '#__next > div.styles_root__nRLZC > div.styles_root__BJH2_.styles_headerContainer__f7XqC > header > div > div.styles_mainContainer__faOVn.styles_hasSidebar__rU_E2 > div.styles_searchFormContainerWide__3taA3.styles_searchFormContainer__GyAL5 > div > form > div > div > button > svg')  # search element by css selector
          findactor.click()
          # find2 = browser.find_element(By.CSS_SELECTOR,
          #                              '#block_left_pad > div > div:nth-child(3) > div > div.info > p > a')  # search element by css selector
          # find2.click()

            # move to actors page
          movetoactor = browser.find_element(By.CSS_SELECTOR,
                                       '#block_left_pad > div > div:nth-child(3) > div > div.info > p > a')  # search element by css selector
          movetoactor.click()
          # find3 = browser.find_element(By.CLASS_NAME,
          #                              'styles_title__qKISE')  # search element by css selector
          # find3.click()
          actrs = []
          soup = BeautifulSoup(browser.page_source, 'html.parser')

          act = soup.find_all('ul', class_='styles_list___ufg4') #search for all actors for movie

            #take actor links with html
          for actors in act:
             if actors:
                # actrs1 = actors.text.strip()
                # actrs.append(str(actrs1))
                actorsaa = [link1 for element in soup.find_all('ul',class_='styles_list___ufg4') for elem in element.find_all('li') for link1 in elem.find_all('a')]
                linkarr = []
                for href in actorsaa:
                    linkarr.append(href.get('href'))

            # take all actor's links text
                for linkActors in linkarr:
                    browser.get("https://www.kinopoisk.ru"+linkActors)
                    soup2 = BeautifulSoup(browser.page_source, 'html.parser')
                    print(soup2.find_all('h1'))
                    names=soup2.find('h1').text.strip()
                    # search for photos
                    driver = webdriver.Chrome()
                    driver.get("https://www.kinopoisk.ru/?utm_referrer=yandex.by")
                    search = driver.find_element(By.NAME, 'kp_query')  # search element by name
                    search.send_keys(names)  # enter prompt in the search field
                    findactor = browser.find_element(By.CSS_SELECTOR,
                                                '#__next > div.styles_root__nRLZC > div.styles_root__BJH2_.styles_headerContainer__f7XqC > header > div > div.styles_mainContainer__faOVn.styles_hasSidebar__rU_E2 > div.styles_searchFormContainerWide__3taA3.styles_searchFormContainer__GyAL5 > div > form > div > div > button > svg')  # search element by css selector
                    findactor.click()
                    # wait for results
                    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'search_results')))

                    link = driver.find_element(By.CSS_SELECTOR,
                                               '#block_left_pad > div > div:nth-child(3) > div > div.info > p > a')
                    actor_url = link.get_attribute('href')
                    driver.get(actor_url)

                    div = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'styles_photo__Is7OJ')))

                    # Получаем ссылку на изображение из атрибута src тега img
                    img_src = div.find_element(By.TAG_NAME, 'img').get_attribute('src')

                    # Скачиваем изображение по ссылке
                    response = requests.get(img_src)
                    print(img_src)

                    # actrs1 = actors.text.strip()
                    # actrs.append(str(actrs1))
                    #for el in soup2.find_all('img',attrs={'srcset':True}):
                      #  print(el['srcset'])
                    # print(pic)
                    # bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-kinopoisk-image…3646/3acd328c-721a-47ac-a7bf-fe7d5efb69fc/280x420')



                # elements = [element.text.strip() for element in soup.find_all('li')]
                #
                # result = ' '.join(elements)
                # result=str(result)


             else:
                actrs1 = "Not found"
                actrs.append(actrs1)
             # for i in range(len(actrs)):
             #         for c in range(len(alf)):
             #                  if actrs[i]==Alf[c]:
             #                           print(i)

          # str= series[find('/">'):find('</a>')]
          # str1=str(series)
          # pos =str1.find('<div class="num">1.</div>')
          # print(pos)
          # bot.send_message(message.chat.id, soup2.find_all('img'))
  # for i in range(len(actrs)):
  #                     for c in range(len(alf)):
  #                        if actrs[i]==Alf[c]:
  #                           print('a')

bot.polling()

# Попробуйте изменить запрос. Многие фильмы имеют несколько названий, а фамилии актеров — разные варианты написаний на русском языке.