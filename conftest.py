import pytest
import os
from zipfile import ZipFile


CURRENT_FILE = os.path.abspath(__file__)  # местоположение текущего файла
print(CURRENT_FILE)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)  # текущая директория
print(CURRENT_DIR)

TMP_DIR = os.path.join(CURRENT_DIR, "download")  # указание директории для скачивания файла
print(TMP_DIR)


@pytest.fixture()
def create_zip_file():
    os.makedirs(TMP_DIR, exist_ok=True)
    with ZipFile(f"{TMP_DIR}/archive.zip", mode="w") as zip_archive:
        zip_archive.write("file/pdf_file.pdf", "pdf_file.pdf")
        zip_archive.write("file/csv.csv", "csv.csv")
        zip_archive.write("file/import_ou_xls.xlsx", "import_ou.xlsx")
    yield
    os.remove(f"{TMP_DIR}/archive.zip")





