import requests
import time
import mysql.connector
import shutil
from bs4 import BeautifulSoup
import pandas as pd

# config connect to database
my_db = mysql.connector.connect(
    host='localhost',
    user="recipe",
    password="recipe",
    database="recipe"
)

data = []
data_full = []

# name column db pandas
# header = ['Назва', 'Категорія', 'Посилання']

def download_image(customurl):
    try:
        name_file = customurl.split('/')
        name_file = 'img/' + name_file[-1]
        img_data = requests.get(customurl).content
        f = open(name_file, 'wb')
        f.write(img_data)
        f.close()
        #time.sleep(0.5)
        #shutil.copy2(name_file, '\\img\\' + name_file)
        return name_file
    except:
        return 'download error'

def parse_site():
    for number_page in range(12, 16):
        # request in web site, parse cart item
        print("parse page " + str(number_page))
        url = "https://rud.ua/consumer/recipe/page=" + str(number_page)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'lxml')
        name = soup.findAll('div', class_='item')

        for names in name:
            # parse config cart item
            recipe_url = "https://rud.ua" + names.find('a').get('href')
            recipe_image = "https://rud.ua" + names.find('img').get('src')
            recipe_name = names.find('div', class_='t').text
            recipe_category = names.find('div', class_='date').text

            data.append((recipe_name, recipe_category, recipe_url, recipe_image))

        time.sleep(0.5)

    # sort product cart in web site
    custom_number = 0
    for recipe in data:
        time.sleep(0.5)
        custom_number += 1
        print('parse page' + str(custom_number))
        url = recipe[2]
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'lxml')

        recipe_name = recipe[0]
        recipe_category = recipe[1].replace("\n", '')
        url_image = recipe[3]


        recipe_image = download_image(url_image)
        print('url image ; ' + recipe_image)

        try:
            recipe_time = soup.find('time').text.replace("\n", '')
        except:
            recipe_time = '-'
        try:
            recipe_level = soup.find('span', class_='easy').text.replace("\n", '')
        except:
            recipe_level = '-'
        try:
            recipe_time_eat = soup.find('span', class_='breakfast').text.replace("\n", '')
        except:
            recipe_time_eat = '-'
        try:
            #parse item list
            name2 = soup.findAll('tr')
            recipe_list_prod = ""
            for i in name2:
                recipe_list_prod += "<p>" + i.text.replace("\n", "") + "</p>\n\r"
        except:
            recipe_list_prod = '-'
        try:
            #parce instruction
            name3 = soup.find('div', class_="center clearfix")
            name4 = name3.findAll('p')
            recipe_instruction = ""
            for i in name4:
                recipe_instruction += "<p>" + i.text.replace("\n", '') + "</p>\n\r"
        except:
            recipe_instruction = '-'

        data_full.append((
            recipe_name,
            recipe_category,
            recipe_time,
            recipe_level,
            recipe_time_eat,
            recipe_list_prod,
            recipe_instruction,
            recipe_image,))


    # df = pd.DataFrame(data, columns=header)
    # df.to_csv("data.csv", sep=';', encoding='utf8')
    print('create dump web site !')


def import_sql():
    '''
        mycursor = my_db.cursor()
        sql = "INSERT INTO all_list (name, category, url) VALUES (%s, %s, %s)"
        val = data
        mycursor.executemany(sql, val)
        my_db.commit()
    '''

    mycursor = my_db.cursor()
    sql = "INSERT INTO full_list (name, category, time_cookie, level, time_eat, list_prod, instruction, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = data_full
    mycursor.executemany(sql, val)
    my_db.commit()



if __name__ == '__main__':
    parse_site()
    time.sleep(2)
    import_sql()
