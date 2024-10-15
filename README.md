Задать папку для скачивания по-умолчанию.
---
from selenium import webdriver 


options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": TMP_DIR,

    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
browser.config.driver_options = options

---
Открыть и записать a файл значение
---
with open("hello.txt", "a") as example_file:  # 'w' - перезаписывает файл, 'а' - дозаписывает в конце файла
    example_file.write("Hello World\n")

----
Работа с путями
---
import os

CURRENT_FILE = os.path.abspath(__file__)  # местоположение текущего файла
print(CURRENT_FILE)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)  # текущая директория

print(CURRENT_DIR)

TMP_DIR = os.path.join(CURRENT_DIR, "download")  # указание директории для скачивания файла
print(TMP_DIR)

---
Чтение из PDF-файла
---
from pypdf import PdfReader

reader = PdfReader("download_file/Smoke.pdf")

print(reader.pages)  # список объектов страниц

print(len(reader.pages))  # количество страниц в файле

print(reader.pages[0].extract_text())  # печатает содержимое страницы

---
Чтение из XLSX-файла
from openpyxl import load_workbook

workbook = load_workbook("download_file/fake_and_links.2024-09-26 10_48_19.216625 (1).xlsx")

sheets = workbook.sheetnames  # список листов
for sheet in sheets:
    print(sheet)

sheet = workbook.active  # получаем активный лист

print(sheet["A1"].value)  # печатаем значение ячейки A1
print(sheet["B1"].value)  # печатаем значение ячейки B1

sheet2 = workbook["Фейки"]  # получаем другой лист(в скобках название листа)
print(sheet2["A1"].value)  # печатаем значение ячейки A1 листа sheet2

workbook.active = 0  # делаем 3 лист активным

cell = sheet["C1"]
print('Строка: ' + str(cell.row))       # номер строки
print('Столбец: ' + str(cell.column))   # номер столбца
print('Ячейка: ' + cell.coordinate)     # местоположение ячейки

cell = sheet.cell(row=1, column=4)      # получаем значение из 2 строки и 3 столбца
print(cell.value)

for cell in sheet['E']:  # все значения из указанной колонки
    print(cell.value)

---
Чтение из XLS-файла
---

from xlrd import open_workbook

workbook = open_workbook("download_file/import_ou_xls.xls")

print(workbook.nsheets)         # количество листов
print(workbook.sheet_names())   # имена листов

sheet = workbook.sheet_by_index(0)  # имя листа
print(sheet)

print(sheet.ncols)  # количество колонок на листе
print(sheet.nrows)  # количество строк на листе

print(sheet.cell_value(rowx=3, colx=2))     # достать значение из ячеки 4 строки 2 колонки

for rx in range(sheet.nrows):               # распечатать строки полностью
    print(sheet.row(rx))

---
Работа с CSV файлом
---
import csv

with open("./download_file/csv.csv") as csv_file:  # открываю файл
    reader = csv.reader(csv_file)                  # указываю, что буду работать с этим файлом с помощью библиотеки csv
    for row in reader:                             # построчная печать из файла
        print(row)

with open("./download_file/csv.csv") as csv_file:
    reader = csv.DictReader(csv_file, delimiter=",")
    for row in reader:                             # печать значений их указанной колонки
        print(row['Название'])