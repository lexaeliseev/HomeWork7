from pypdf import PdfReader
from zipfile import ZipFile
from conftest import TMP_DIR
from openpyxl import load_workbook
import csv


# def test_check_pdf(create_zip_file):
#     with ZipFile(f"{TMP_DIR}/archive.zip") as zip_file:
#         print(zip_file.namelist())
#         with zip_file.open("pdf_file.pdf") as pdf_file:
#             reader = PdfReader(pdf_file)
#             assert len(reader.pages) == 1
#
#             check_text = reader.pages[0].extract_text().strip()
#             # print(check_text)
#             # assert "Hello,World" in check_text


# def test_check_xlsx(create_zip_file):
#     with ZipFile(f"{TMP_DIR}/archive.zip") as zip_file:
#         with zip_file.open("import_ou.xlsx") as xlsx_file:
#             workbook = load_workbook(xlsx_file)
#
#             print("---")
#             count_pages = len(workbook.sheetnames)
#             print(f"Количество листов в книге: {count_pages}")
#             assert count_pages == 1
#             print("---")
#
#             sheet = workbook.active
#             print(f"Название активного листа: {sheet.title}")
#             assert sheet.title == "TemplateImportOU"
#
#             cell_value = sheet['C1'].value
#             print(f"Значение ячейки: {cell_value}")
#             assert cell_value == "Название"


def test_check_csv(create_zip_file):
    with ZipFile(f"{TMP_DIR}/archive.zip") as zip_file:
        with zip_file.open("csv.csv") as csv_file:
            content = csv_file.read().decode('utf-8-sig')
            reader = list(csv.reader(content.splitlines()))

            print("---")
            first_row = reader[0]
            count_columns = len(first_row)
            print(f"Количество колонок: {count_columns}")
            assert count_columns == 3

            print("---")
            value = "Внешний идентификатор для импорта,Вышестоящий отдел,Название"
            list_value = value.split(",")
            print(f"Список заголовков: {first_row}")
            assert first_row == list_value

            print("---")
            count_row = sum(1 for _ in reader)
            print(f"Количество строк в файле: {count_row}")
            assert count_row == 7

