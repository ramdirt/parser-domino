# -*- coding: utf8 -*-
from functions import *
from check_were_added import *

setting = Settings()

def main():
    url = setting.url_catalog
    text = get_html(url)
    get_catalog_data(text)

def get_page_data(html):
    description = description_refine('desc', html)
    attribute = parts_attribute_refine('attributi', html)
    area_of_use = area_of_use_refine('cnt_settore', html)
    applicazioni = applicazioni_refine('col-sm-12 mt-3', html)

    image_url = get_image_url('col-sm-7', html)
    image_schema_url = get_image_url('my-4', html)

    return {'description': description,
            'attribute': attribute,
            'image_url': image_url,
            'area_of_use': area_of_use,
            'applicazioni': applicazioni,
            'image_schema_url': image_schema_url}

def get_catalog_data(html):
    page_catalog = BeautifulSoup(html, 'lxml') # получаем код страницы
    blocks = page_catalog.find_all('div', {'class':'col col-sm-6 col-md-4 col-lg-3'}) # инициализируем плитки товаров
    title = ' '.join(page_catalog.find('h1').text.lstrip().rstrip().capitalize().split()) # получаем название каталога

    for block in blocks[setting.range_min:setting.range_max]:
        code = block.find('div', {'class': 'code'}).text # получаем код товара
        parts_url = setting.url_domen + block.find('a').get('href') # получаем ссылку на товар
        name_parts = block.find('div', {'class': 'name'}).text # получаем название товара

        data_added_parts = copy_check() # инициализируем список товаров которые были добавлены, чтобы избавится от копий
        """Делаем проверку на копию, если ок, то добавляем товар в CSV, если нет, то пропускаем"""
        try:
            if data_added_parts[code]:
                print('Данный товар уже был добавлен')
                continue
        except:
            write_were_added({'code': code, 'url': parts_url})


        parts_info = get_page_data(get_html(parts_url))
        description = parts_info['description']
        attribute = parts_info['attribute']
        applicazioni = parts_info['applicazioni']
        image_url = parts_info['image_url']
        schema_url = image_schema_refine(parts_info['image_schema_url'])
        area = ''.join([f'{title[0:11]}/{i};' for i in parts_info['area_of_use']])


        data = {'Tilda UID': code,
                'SKU': code,
                'Category': area[0:-1],
                'Title': name_parts,
                'Description': description,
                'Text': description + '<br>' + attribute + applicazioni + schema_url,
                'Photo': image_url,
                'Price': cost_parts(code),
                'Quantity': 0,
                'External ID': code
                }

        try:
            write_csv(data)
            print('Данные получены: ' + code)
        except:
            print('Данные не получены: ' + code)



if __name__ == '__main__':
    title_csv()
    main()