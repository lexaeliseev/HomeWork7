from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": TMP_DIR,

    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
browser.config.driver_options = options

---

with open("hello.txt", "a") as example_file:  # 'w' - перезаписывает файл, 'а' - дозаписывает в конце файла
    example_file.write("Hello World\n")

----

import os

CURRENT_FILE = os.path.abspath(__file__)  # местоположение текущего файла
print(CURRENT_FILE)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)  # текущая директория
print(CURRENT_DIR)

TMP_DIR = os.path.join(CURRENT_DIR, "download")  # указание директории для скачивания файла
print(TMP_DIR)

---

from pypdf import PdfReader

reader = PdfReader("download_file/Smoke.pdf")

print(reader.pages)  # список объектов страниц

print(len(reader.pages))  # количество страниц в файле

print(reader.pages[0].extract_text())  # печатает содержимое страницы

---

