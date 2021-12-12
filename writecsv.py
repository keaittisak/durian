import csv


def writecsv(data):
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
    print('Success')


d = ['2021-05-11 10:15:10', 50, 50]
writecsv(d)
