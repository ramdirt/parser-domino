from settings import *
import requests
from bs4 import BeautifulSoup
from functions import *

config = Settings()

def view_table(table):
    for i in table:
        print(i)
def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        print(r.status_code)
def url_img_refine(url):
    try:
        return config.url_domen + url.get('src').replace(' ','%20').replace('(', '%28').replace(')', '%29')
    except:
        return 'https://www.domino-group.com/tommaselli/img/logo/Logo-Tommaselli.png'

def main():
    catalog = Catalog(config.url_catalog)
    catalog.init_catalog()
    print(catalog.data[30])
    page = Page(catalog.data[30])
    page.init_page()

class Catalog():
    def __init__(self, url_catalog):
        self.url_catalog = url_catalog
        self.data = []
    def init_catalog(self):
        catalog = BeautifulSoup(get_html(self.url_catalog), 'lxml')
        blocks = catalog.find_all('div', {'class': 'col col-sm-6 col-md-4 col-lg-3'})
        for block in blocks:
            name_parts = block.find('div', {'class': 'name'}).text
            code_parts = block.find('div', {'class': 'code'}).text
            url_parts = block.find('a').get('href')

            self.data.append({'name_parts': name_parts,
                              'code_parts': code_parts,
                              'url_parts': url_parts
                             })

class Page():
    def __init__(self, data):
        self.name_parts = data['name_parts']
        self.code_parts = data['code_parts']
        self.url_parts = config.url_domen + data['url_parts']

    def init_page(self):
        page = BeautifulSoup(get_html(self.url_parts), 'lxml')

        name_catalog = page.find('h1').text.lstrip().rstrip().capitalize()
        type_parts = page.find('h2', {'class': 'title'}).text.capitalize()
        description = page.find('div', {'class': 'desc'}).text.lstrip().rstrip().capitalize()
        attribute = [i.text for i in page.find_all('li', {'class': 'my-2'})]
        use_area = [i.text.lstrip().rstrip() for i in page.find('div', {'class': 'cnt_settore'}).find_all('li')]
        image_url = url_img_refine(page.find('img', {'class': 'w-100'}))
        image_schema_url = url_img_refine(page.find('img', {'class': 'my-4'}))
        print()
        print(self.url_parts)
        area = ''.join([f'{name_catalog.split()[0]}/{i}/{type_parts};' for i in use_area])
        print(area)



if __name__ == '__main__':
    main()