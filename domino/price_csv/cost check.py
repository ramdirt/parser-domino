import csv

code_and_price = []

def write_csv(data):
    with open('price_domino_relevant.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['code'],
                         data['price'],
                         ))

with open('price_domino.csv') as file:
    fieldnames = ['code', 'price', 'none']
    reader = csv.DictReader(file, fieldnames=fieldnames, delimiter = ";")

    for row in reader:
        code_and_price.append([row['code'], row['price'].replace(',', '.')])

for i in code_and_price:
    data = {'code': i[0],
            'price': float(i[1])}

    write_csv(data)






