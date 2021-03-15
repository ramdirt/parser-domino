import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def main():
    url = 'https://www.domino-group.com/tommaselli/en/foldable-lever-assembly-f-33-4139-04-00.html?idct=183'
    get_page_data(get_html(url))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    type_parts = soup.find('h2', {'class': 'title'}).text
    description = soup.find('div', {'class': 'desc'}).text.lstrip().rstrip()
    parts_attribute = soup.find('div', {'class': 'attributi'})
    parts_attribute = parts_attribute.find_all('li')
    part_att = ''
    for i in parts_attribute:
        part_att += str(i.text) + '\n'
    area_of_use = soup.find('div', {'class': 'cnt_settore'}).find('li').text.lstrip()

    data = {'type_parts': type_parts,
            'description': description,
            'part_att': part_att,
            'area_of_use': area_of_use
            }

    write_csv(data)

def write_csv(data):
    with open('domino_parts', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['type_parts'],
                         data['description'],
                         data['part_att'],
                         data['area_of_use']))

if __name__ == '__main__':
    main()