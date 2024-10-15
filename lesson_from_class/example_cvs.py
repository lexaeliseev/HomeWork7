import csv

with open("./download_file/csv.csv") as csv_file:  # открываю файл
    reader = csv.reader(csv_file)                  # указываю, что буду работать с этим файлом с помощью библиотеки csv
    for row in reader:                             # построчная печать из файла
        print(row)

with open("./download_file/csv.csv") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=",")
    for row in reader:                             # печать значений их указанной колонки
        print(row['Название'])
