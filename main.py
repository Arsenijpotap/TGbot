import json
import telebot
from selenium import webdriver

from selenium.webdriver.common.by import By


bot = telebot.TeleBot('5820951961:AAHPNgrfEvQ-mHlnR74p3YkkpEheUL7W1Vo')
keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('найти контент по актеру', 'найти актеров по контенту','найти информацию об актёре')
keybord1.row('список избранного', 'завершить')
keybord2 = telebot.types.ReplyKeyboardMarkup(True)
keybord2.row('избранные актеры', 'избранный контент', 'обратно')
keybord3 = telebot.types.ReplyKeyboardMarkup(True)
keybord3.row('список избранных актеров', 'обратно')
keybord4 = telebot.types.ReplyKeyboardMarkup(True)
keybord4.row('список избранного контента', 'обратно')
cnt = 1
a = 10
b = 0
@bot.message_handler(commands=['start'])
def start_message(message):
   global user
   user = message.chat.id
   bot.send_message(message.chat.id, 'что вы хотите сделать?', reply_markup=keybord1)
   print(id)
   s = 0
   with open('json.json', 'r') as f:
       data = json.load(f)
       for item in data:
           for key in item:
               if key != str(message.chat.id):
                   s += 1
       if s == len(data):
           data.append({message.chat.id: ["1"]})
           with open('json.json', 'w') as f:
               json.dump(data, f)
       print(data)
   s = 0
   with open('cont.json', 'r') as fl:
       data2 = json.load(fl)
       for item in data2:
           for key in item:
               if key != str(message.chat.id):
                   s += 1
       if s == len(data2):
           data2.append({message.chat.id: ["1"]})
           with open('cont.json', 'w') as fl:
               json.dump(data2, fl)
       print(data2)


@bot.message_handler(content_types=['text'])
def start_message1(message):
   global a
   if message.text == 'найти актеров по контенту':
       bot.send_message(message.chat.id, 'хорошо, введите название контента')
       counter = 1
       a = 1










   elif message.text == 'найти контент по актеру':

       bot.send_message(message.chat.id, 'хорошо, введите имя и фамилию актера')
       a = 2



   elif message.text == 'список избранного':
       bot.send_message(message.chat.id, 'хорошо', reply_markup=keybord2)
       a=11




   elif message.text == 'завершить':
       bot.send_message(message.chat.id, 'до встречи')
       a=0
   elif message.text == 'найти информацию об актёре':
       bot.send_message(message.chat.id, 'хорошо, введите имя и фамилию актера')
       a=3
   elif message.text == 'обратно':
       bot.send_message(message.chat.id, 'хорошо', reply_markup=keybord1)
       start_message(message)
   elif a ==1:

       def searchactorsbyfilm():
           message.text = str(message.text).title()
           browser = webdriver.Edge()
           browser.get("https://www.kino-teatr.ru/")
           search = browser.find_element(By.NAME, 'text')  # search element by name
           search.send_keys(message.text)  # enter prompt in the search field
           findactor = browser.find_element(By.CSS_SELECTOR,
                                        '#search_button')  # search element by css selector
           findactor.click()
           grid = browser.find_element(By.XPATH, '//*[@id="all_body_block"]/div[4]/div/div[3]/div[1]/div[5]')
       # Извлекаем информацию из ячеек сетки и формируем словарь с именами актеров и ссылками на них
           actor_dict = {}
           o=0
           for cell in grid.find_elements(By.TAG_NAME, "div"):
               actor_names = cell.find_elements(By.XPATH,
                                                '//*[@id="all_body_block"]/div[4]/div/div[3]/div[1]/div[5]/div[2]/div[2]/div[5]/span')
               o += 1
               if o == 3:
                   break
               for actor_name in actor_names:
                   actor_text = actor_name.text.strip()

                   if o == 1:
                       break
                   if actor_text != "Актеры:":
                       actor_links = actor_name.find_elements(By.TAG_NAME, "a")
                       for actor_link in actor_links:
                           actor_dict[actor_text] = actor_link.get_attribute("href")
                           if o == 1:
                               break

           for value in actor_dict.values():
               bot.send_message(message.chat.id,value)


           print(actor_dict)


       searchactorsbyfilm()

   elif a==3:
       def searchinfo():
           message.text = str(message.text).title()
           browser = webdriver.Edge()
           browser.get("https://www.kino-teatr.ru/")
           search = browser.find_element(By.NAME, 'text')  # search element by name
           search.send_keys(message.text)  # enter prompt in the search field
           findactor = browser.find_element(By.CSS_SELECTOR,
                                            '#search_button')  # search element by css selector
           findactor.click()

           if browser.find_element(By.CSS_SELECTOR,
                                          '#all_body_block > div.center_1200_to_320 > div > div:nth-child(5) > div.content_block > div:nth-child(5) > div:nth-child(2) > div.list_item_details > div.list_item_content > div > a'):


               findact = browser.find_element(By.CSS_SELECTOR,
                                          '#all_body_block > div.center_1200_to_320 > div > div:nth-child(5) > div.content_block > div:nth-child(5) > div:nth-child(2) > div.list_item_details > div.list_item_content > div > a')
               findact.click()
           #
               if browser.find_element(By.XPATH,
                                               '//*[@id="all_body_block"]/div[4]/div/div[2]/div[2]/div[1]/div[5]/div[2]'):
                   findinfo = browser.find_element(By.XPATH,
                                                   '//*[@id="all_body_block"]/div[4]/div/div[2]/div[2]/div[1]/div[5]/div[2]')
                   # создаем пустой список и ищем весь текст из биографии актера
                   actor_info = []
                   actor_infotext = findinfo.find_elements(By.TAG_NAME, 'div')
                   pos= 0
                   for i in actor_infotext:
                       actor_info.append(i.text.strip())
                       print(i.text.strip().split('\n'))
                       pos=i.text.strip().find('.',3900,4000)
                   act=actor_info[1]
                   pos=act.find('.',3900,4000)
                   print( str(act[:pos])+'.')
                   bot.send_message(message.chat.id, str(act[:pos])+'.')
                   act = actor_info[3]
                   pos = act.find(' ', 3900, 4000)
                   bot.send_message(message.chat.id, str(act[:pos]))
                   act = actor_info[4]
                   pos = act.find(' ', 3900, 4000)
                   bot.send_message(message.chat.id, str(act[:pos]) + '.')

                   # for r in range(len(i.text.strip().split(')'))):
                   #     if i.text.strip()==' ':
                   #         continue


                   # pos=i.text.strip().find('.',3900,4000)
               # bot.send_message(message.chat.id,i.text.strip())



               # теперь ищем его фото
               img_src = browser.find_element(By.XPATH, '//img[@id="main_photo_md"]').get_attribute('src')
               # actor_info.append(img_src)


               # Получаем список

       searchinfo()
#browser.quit()
# act = soup.find("div", )  # search for all actors for movie
# #
# # take actor links with html
# for actor in act:
#     name = actor.find_all("span", itemprop="name").text
#     print(name)
#
# # find2 = browser.find_element(By.CSS_SELECTOR,
#                              '#block_left_pad > div > div:nth-child(3) > div > div.info > p > a')  # search element by css selector
# find2.click()

# move to actors page
# movetoactor = browser.find_element(By.CSS_SELECTOR,
#                                    '#block_left_pad > div > div:nth-child(3) > div > div.info > p > a')  # search element by css selector
# movetoactor.click()
# # find3 = browser.find_element(By.CLASS_NAME,
# #                              'styles_title__qKISE')  # search element by css selector
# # find3.click()
#
   elif a ==2:

       def searchfilms():
           message.text = str(message.text).title()
           browser = webdriver.Edge()
           browser.get("https://www.kino-teatr.ru/")
           search = browser.find_element(By.NAME, 'text')  # search element by name
           search.send_keys(message.text)  # enter prompt in the search field
           findactor = browser.find_element(By.CSS_SELECTOR,
                                            '#search_button')  # search element by css selector
           findactor.click()
           findact = browser.find_element(By.CSS_SELECTOR,
                                            '#all_body_block > div.center_1200_to_320 > div > div:nth-child(5) > div.content_block > div:nth-child(5) > div:nth-child(2) > div.list_item_details > div.list_item_content > div > a')
           findact.click()
           # # если актер есть в списке, мы можем получить информацию
           #
           findinfo = browser.find_element(By.XPATH, '//*[@id="all_body_block"]/div[4]/div/div[2]/div[2]/div[1]/div[5]/div[2]')

           print("Список популярных фильмов и сериалов актера")
           moviesandseries = []
           movies = browser.find_element(By.XPATH, '//*[@id="all_body_block"]/div[4]/div/div[2]/div[2]/div[2]/div[4]')

           lnks = movies.find_elements(By.CSS_SELECTOR, "a.block_online_right_item")

           for lnk in lnks:
               movietitle = lnk.get_attribute("title")
               movieurl = lnk.get_attribute('href')
               try:
                   movieimg = lnk.find_element(By.CSS_SELECTOR, 'span.block_online_right_item_img').get_attribute(
                       "style")

                   movieimg = movieimg.strip().replace('background-image: url(', '').replace(')', '').replace('"', '')
               except:
                   movieimg = None

               moviesandseries.append({"title": movietitle, "url": movieurl,
                                       "image": f"https://www.kino-teatr.ru{movieimg.replace('/', '//')}"})

           for m in moviesandseries:
               bot.send_message(message.chat.id, m["title"])
               bot.send_message(message.chat.id, m["url"])
               # bot.send_message(message.chat.id, m["image"])
               print("---------------")

       searchfilms()

   elif message.text == 'избранные актеры':
       bot.send_message(message.chat.id,'чтобы добавить/удалить актера в избранное напишине его имя и фамилию ', reply_markup=keybord3)
       a = 4

   elif a == 4:
       message.text = str(message.text).title()
       with open('json.json', 'r') as f:
           data = json.load(f)
           for item in data:

               for key in item:
                   if key== str(message.chat.id):

                       if message.text!='обратно' and message.text!='избранные актеры' and message.text!='избранный контент' and message.text!='список избранных актеров' and message.text!='список избранного контента':

                           c=0
                           item[str(message.chat.id)].append("|")
                           bot.send_message(message.chat.id, 'список избранных актеров:')
                           for elem in item[str(message.chat.id)]:
                               print(elem)
                               if elem == str(message.text):
                                   item[str(message.chat.id)].remove(message.text)
                               elif not elem== str(message.text):
                                   c+=1
                               if c == len( item[str(message.chat.id)]):
                                   item[str(message.chat.id)].append(message.text)
                           item[str(message.chat.id)].remove("|")
                           print(item[str(message.chat.id)])
                           with open('json.json', 'w') as f:
                               json.dump(data, f)
                           for i in range(len(item[str(message.chat.id)])-1):

                               browser = webdriver.Edge()
                               browser.get("https://www.kino-teatr.ru/")
                               search = browser.find_element(By.NAME, 'text')  # search element by name
                               search.send_keys(item[str(message.chat.id)][i+1])  # enter prompt in the search field
                               findactor = browser.find_element(By.CSS_SELECTOR,
                                                                '#search_button')  # search element by css selector
                               findactor.click()
                               if browser.find_element(By.CSS_SELECTOR,
                                                       '#all_body_block > div.center_1200_to_320 > div > div:nth-child(5) > div.content_block > div:nth-child(5) > div:nth-child(2) > div.list_item_details > div.list_item_content > div > a'):
                                   findact = browser.find_element(By.CSS_SELECTOR,
                                                                  '#all_body_block > div.center_1200_to_320 > div > div:nth-child(5) > div.content_block > div:nth-child(5) > div:nth-child(2) > div.list_item_details > div.list_item_content > div > a')
                                   findact.click()
                               #

                                   img_src = browser.find_element(By.XPATH, '//img[@id="main_photo_md"]').get_attribute('src')
                                   print(img_src)
                                   bot.send_photo(message.chat.id,img_src )
                                   bot.send_message(message.chat.id, item[str(message.chat.id)][i + 1])
                           if len(item[str(message.chat.id)])==1:
                               bot.send_message(message.chat.id, 'Список избранных актеров пуст.\nЧтобы добавить актера в избранное напишине его имя и фамилию')
                       elif str(message.text)=='список избранных актеров':
                           for i in range(len(item[str(message.chat.id)])-1):

                               browser = webdriver.Edge()
                               browser.get("https://www.kino-teatr.ru/")
                               search = browser.find_element(By.NAME, 'text')  # search element by name
                               search.send_keys(item[str(message.chat.id)][i + 1])  # enter prompt in the search field
                               findactor = browser.find_element(By.CSS_SELECTOR,
                                                                '#search_button')  # search element by css selector
                               findactor.click()
                               if browser.find_element(By.CSS_SELECTOR,
                                                       '#all_body_block > div.center_1200_to_320 > div > div:nth-child(5) > div.content_block > div:nth-child(5) > div:nth-child(2) > div.list_item_details > div.list_item_content > div > a'):
                                   findact = browser.find_element(By.CSS_SELECTOR,
                                                                  '#all_body_block > div.center_1200_to_320 > div > div:nth-child(5) > div.content_block > div:nth-child(5) > div:nth-child(2) > div.list_item_details > div.list_item_content > div > a')
                                   findact.click()
                                   #

                                   img_src = browser.find_element(By.XPATH,
                                                                  '//img[@id="main_photo_md"]').get_attribute('src')
                                   print(img_src)
                                   bot.send_photo(message.chat.id, img_src)
                                   bot.send_message(message.chat.id, item[str(message.chat.id)][i + 1])
                           if len(item[str(message.chat.id)])==1:
                               bot.send_message(message.chat.id, 'Список избранных актеров пуст.\nЧтобы добавить актера в избранное напишине его имя и фамилию')

   elif message.text == 'избранный контент':
       bot.send_message(message.chat.id, 'чтобы добавить/удалить контент в избранное напишине название ',
                        reply_markup=keybord4)
       a = 5

   elif a == 5:
       message.text = str(message.text).title()
       with open('cont.json', 'r') as fl:
           data = json.load(fl)
           for item in data:

               for key in item:
                   if key == str(message.chat.id):

                       if message.text != 'обратно' and message.text != 'избранные актеры' and message.text != 'избранный контент' and message.text != 'список избранных актеров':

                           c = 0
                           item[str(message.chat.id)].append("|")
                           bot.send_message(message.chat.id, 'список избранного контента:')
                           for elem in item[str(message.chat.id)]:
                               print(elem)
                               if elem == str(message.text):
                                   item[str(message.chat.id)].remove(message.text)
                               elif not elem == str(message.text):
                                   c += 1
                               if c == len(item[str(message.chat.id)]):
                                   item[str(message.chat.id)].append(message.text)
                           item[str(message.chat.id)].remove("|")
                           print(item[str(message.chat.id)])
                           with open('cont.json', 'w') as f:
                               json.dump(data, f)
                           for i in range(len(item[str(message.chat.id)]) - 1):

                               browser = webdriver.Edge()
                               browser.get("https://www.kino-teatr.ru/")
                               search = browser.find_element(By.NAME, 'text')  # search element by name
                               search.send_keys(item[str(message.chat.id)][i + 1])  # enter prompt in the search field
                               findff = browser.find_element(By.CSS_SELECTOR,
                                                                '#search_button')  # search element by css selector
                               findff.click()
                               findfl = browser.find_element(By.XPATH,
                                                                  '//*[@id="all_body_block"]/div[4]/div/div[3]/div[1]/div[5]/div[2]/div[2]/div[1]/h4/a[1]')
                               findfl.click()



                               img_src = browser.find_element(By.XPATH,
                                                                  '//*[@id="main_photo"]').get_attribute('src')
                               print(img_src)
                               bot.send_photo(message.chat.id, img_src)
                               bot.send_message(message.chat.id, item[str(message.chat.id)][i + 1])
                           if len(item[str(message.chat.id)]) == 1:
                               bot.send_message(message.chat.id,
                                                'Список избранного контента пуст.\nЧтобы добавить контент в избранное напишине его название')
                       elif str(message.text) == 'список избранного контента':
                           for i in range(len(item[str(message.chat.id)]) - 1):

                               browser1 = webdriver.Edge()
                               browser1.get("https://www.kino-teatr.ru/")
                               search = browser1.find_element(By.NAME, 'text')  # search element by name
                               search.send_keys(item[str(message.chat.id)][i + 1])  # enter prompt in the search field
                               findff = browser1.find_element(By.CSS_SELECTOR,
                                                                '#search_button')  # search element by css selector
                               findff.click()
                               findfl = browser.find_element(By.XPATH,
                                                                  '//*[@id="all_body_block"]/div[4]/div/div[3]/div[1]/div[5]/div[2]/div[2]/div[1]/h4/a[1]')
                               findfl.click()



                               img_src = browser.find_element(By.CSS_SELECTOR,
                                                                  '#main_photo')
                               print(img_src)
                               bot.send_photo(message.chat.id, img_src)
                               bot.send_message(message.chat.id, item[str(message.chat.id)][i + 1])
                           if len(item[str(message.chat.id)]) == 1:
                               bot.send_message(message.chat.id,
                                                'Список избранного контента пуст.\nЧтобы добавить контент в избранное напишине его название')







   elif a == 0 :
       bot.send_message(message.chat.id,'некорректный ввод')


bot.infinity_polling()

