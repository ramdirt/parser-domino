# -*- coding: utf8 -*-
from settings import *
import requests
from bs4 import BeautifulSoup
import csv

setting = Settings()
data_cost = []
cost_index = 0

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)

def write_csv(data):
    with open(setting.file_save, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['Tilda UID'],
                         data['SKU'],
                         data['Category'],
                         data['Title'],
                         data['Description'],
                         data['Text'],
                         data['Photo'],
                         data['Price'],
                         data['Quantity'],
                         data['External ID']
                         ))

def parts_attribute_refine(div, html):
    soup = BeautifulSoup(html, 'lxml')
    parts_attribute = soup.find('div', {'class': div}).find_all('li')
    part_att = ''
    for i in parts_attribute:
        part_att += f'{i.text} <br>'
    return part_att

def title_refine(title):
    if title == 'Lever assembly':
        return 'Ручка сцепления с кронштейном'
    elif title == 'Levers':
        return 'Рычаг'
    else:
        return title

def title_catalog_refine(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        type_parts = soup.find('h1').text.lstrip().rstrip().capitalize()
        return type_parts
    except:
        return 'Нет раздела'

def type_parts_refine(type):
    if type == 'Racing with anticorodal levers':
        return 'Гоночный рычаг сцепления из высокопрочного алюминиевого сплата Anticorodal®, обладает чрезвычайно высокой прочностью и способен выдержать усилие в 20 тонн на квадратный дюйм'

def title_csv():
    data = {'Tilda UID': 'Tilda UID',
            'Brand': 'Brand',
            'SKU': 'SKU',
            'Mark': 'Mark',
            'Category': 'Category',
            'Title': 'Title',
            'Description': 'Description',
            'Text': 'Text',
            'Photo': 'Photo',
            'Price': 'Price',
            'Quantity': 'Quantity',
            'External ID': 'External ID'
            }
    write_csv(data)


def cost_parts(code):
    code_parts = str(code[4:])

    with open('price_csv/price_domino_relevant.csv') as file:
        fieldnames = ['code', 'price']
        reader = csv.DictReader(file, fieldnames=fieldnames, delimiter=",")

        for row in reader:
            data_cost.append([row['code'], row['price']])

        cost_index = 0
        for i in data_cost:
            if i[0] == code_parts:
                cost = float(i[1]) * setting.money
                return cost
            elif cost_index == len(data_cost) - 2:
                return '1234'
            else:
                cost_index += 1


        print(data_cost[cost_index][1])

def get_image_url(div, html):
    soup = BeautifulSoup(html, 'lxml')
    if 'div' == 'col-sm-7':
        try:
            image_url = setting.url_domen + soup.find('div',
                                                     {'class': div}).find('img').get('src').replace(' ',
                                                      '%20').replace('(', '%28').replace(')', '%29')
        except:
            image_url = 'https://www.domino-group.com/tommaselli/img/logo/Logo-Tommaselli.png'
    else:
        try:
            image_url = setting.url_domen + soup.find('div',
                                                     {'class': div}).find('img').get('src').replace(' ',
                                                      '%20').replace('(', '%28').replace(')', '%29')
        except:
            image_url = None
    return image_url

def description_refine(div, html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        description = soup.find('div', {'class': div}).text.lstrip().rstrip().capitalize()
        return description
    except:
        description = ''
        return description

def area_of_use_refine(div, html):
    soup = BeautifulSoup(html, 'lxml')
    area = soup.find('div', {'class': div}).find_all('li')
    areas = []
    for i in area:
        areas.append(i.text.lstrip().rstrip().capitalize())
    return areas

def title_parts_refine(div, html):
    soup = BeautifulSoup(html, 'lxml')
    type_parts = soup.find('h2', {'class': div}).text.capitalize()
    return type_parts

def image_schema_refine(url):
    image_schema_url = url
    if image_schema_url != None:
        schema_url = '<br><p><a href={}>Схема</a></p>'.format(image_schema_url)
        return schema_url
    else:
        schema_url = ''
        return schema_url

def applicazioni_refine(div, html):
    soup = BeautifulSoup(html, 'lxml')
    area = soup.find('div', {'class': div}).text.lstrip().rstrip().replace(' ', '')
    return area