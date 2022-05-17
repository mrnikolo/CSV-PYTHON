import csv

with open('data.csv', 'r') as csvfile:
    ''' r is mode reader to dataset'''
    data = csv.reader(csvfile)
    next(data)
    ''' for hide line column in data'''
    for info in data:
        print(info)


with open('data.csv', 'r') as csvfile:
    data = csv.DictReader(csvfile)
    ''' dictReader show detaset like as Dict type '''
    for info in data:
        print(info)
        
with open('dataset.csv', 'w') as csvfile:
    dataset = csv.writer(csvfile, delimiter='-')
    ''' delimiter type show off between datas '''
    dataset.writerow(['product', 'price', 'brand'])
    dataset.writerow(['laptop', '830000', 'asus'])
    dataset.writerow(['hat', '25000', 'nike'])

with open('family.csv', 'w') as csvfile:
    data = csv.DictWriter(csvfile, fieldnames=['father', 'mother', 'sister', 'brother'] , delimiter='|')
    data.writeheader()
    data.writerow({'father': 'ebrahim', 'mother': 'maryam', 'sister': 'sara', 'brother': 'ali'})
    data.writerow({'father': 'hamid', 'mother': 'sabora', 'sister': 'rezieh', 'brother': 'mohsen'})


