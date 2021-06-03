# -*- coding: utf8 -*-
from functions import *
from urllib.request import *
import os
import time

setting = Settings()

def main():
    urls = setting.urls_lever_assembly
    for url in urls:
        get_catalog_data(get_html(url))

def get_catalog_data(html):
    soup = BeautifulSoup(html, 'lxml')
    blocks = soup.find_all('div', {'class':'col col-sm-6 col-md-4 col-lg-3'})

    for block in blocks[setting.range_min:setting.range_max]:
        code = block.find('div', {'class': 'code'}).text.replace(" ", "")
        parts_info = get_page_data(get_html(setting.url_domen + block.find('a').get('href')))
        title = title_catalog_refine(get_html(setting.url_domen + block.find('a').get('href')))

        image_url = parts_info['image_url']
        area_of_use = parts_info['area_of_use'][0]
        type = parts_info['type_parts'].lstrip().rstrip()

        if not os.path.isdir(f'img/{title}/{area_of_use}/{type}'):
            os.makedirs(f'img/{title}/{area_of_use}/{type}')

        if not os.path.isfile(f'img/{title}/{area_of_use}/{type}/{code}.jpg'):
            time.sleep(0)
            urlretrieve(image_url, f'img/{title}/{area_of_use}/{type}/{code}.jpg')
            print(f'Изображение скачано в img/{title}/{area_of_use}/{type} с названием {code}')
        else:
            print('Такой файл есть')

def get_page_data(html):
    type_parts = title_parts_refine('title', html)
    area_of_use = area_of_use_refine('cnt_settore', html)
    image_url = get_image_url('col-sm-7', html)
    image_schema_url = get_image_url('my-4', html)

    return {'image_url': image_url,
            'area_of_use': area_of_use,
            'image_schema_url': image_schema_url,
            'type_parts': type_parts}


if __name__ == '__main__':
    main()