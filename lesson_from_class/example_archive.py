import os
from zipfile import ZipFile
from conftest import TMP_DIR

with ZipFile("download_file/example.zip") as zip_file:
    print(zip_file.namelist())      # список файлов в архиве

    text = zip_file.read("csv.csv")     # чтение из файла в архиве
    print(text)

    zip_file.extract("csv.csv", path=TMP_DIR)         # распаковка файла из архива в указанный раздел

os.remove(TMP_DIR + "/csv.csv")      # удаление файла с указание пути, если нужно
os.rmdir(TMP_DIR)                    # удаление папки
