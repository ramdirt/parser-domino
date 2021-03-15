# -*- coding: utf8 -*-
from functions import *

setting = Settings()

def main():
    url = setting.url_catalog
    text = get_html(url)
    get_catalog_data(text)

def url_img_refine(url):
    try:
        return setting.url_domen + url.get('src').replace(' ','%20').replace('(', '%28').replace(')', '%29')
    except:
        return 'https://www.domino-group.com/tommaselli/img/logo/Logo-Tommaselli.png'

def get_page_data(html):
    page = BeautifulSoup(html, 'lxml')
    description = page.find('div', {'class': 'desc'}).text.lstrip().rstrip().capitalize()
    print(description)
    attribute = [i.text.split(':') for i in page.find_all('li', {'class': 'my-2'})]
    print(attribute)

    return {'description': description,
            'attribute': attribute}

def get_catalog_data(html):
    soup = BeautifulSoup(html, 'lxml')
    blocks = soup.find_all('div', {'class':'col col-sm-6 col-md-4 col-lg-3'})

    for block in blocks[setting.range_min:setting.range_max]:
        name_parts = block.find('div', {'class': 'name'}).text
        print(name_parts)
        code = block.find('div', {'class': 'code'}).text
        print(code)
        parts_url = setting.url_domen + block.find('a').get('href')

        parts_info = get_page_data(get_html(parts_url))
        description = parts_info['description']
        attribute = parts_info['attribute']

        # data = {'Text': description + '<br>' + attribute}

        # try:
        #     write_csv(data)
        #     print('Данные получены: ' + code)
        # except:
        #     data = {'error': code}
        #     write_error_csv(data)
        #     print('Данные не получены: ' + code)

        print()


if __name__ == '__main__':
    title_csv()
    main()