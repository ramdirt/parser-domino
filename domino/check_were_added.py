import csv
from settings import *

setting = Settings()

def write_were_added(data):
    with open(setting.file_were_added, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow((data['code'],
                         data['url'],
                         ))

def copy_check():
    reader = csv.reader(open(setting.file_were_added, 'r'))
    data = {}
    for row in reader:
        key, value = row
        data[key] = value

    return data