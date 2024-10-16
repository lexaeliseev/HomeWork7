from pypdf import PdfReader
from zipfile import ZipFile
from conftest import TMP_DIR
from openpyxl import load_workbook

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


def test_check_xlsx(create_zip_file):
    with ZipFile(f"{TMP_DIR}/archive.zip") as zip_file:
        with zip_file.open("import_ou.xlsx") as xlsx_file:
            workbook = load_workbook(xlsx_file)

            print("---")
            count_pages = len(workbook.sheetnames)
            print(f"Количество листов в книге: {count_pages}")
            assert count_pages == 1
            print("---")

            sheet = workbook.active
            print(f"Название активного листа: {sheet.title}")
            assert sheet.title == "TemplateImportOU"

            cell_value = sheet['A1:C1'].value
            print(f"Значение ячейки: {cell_value}")
            assert cell_value == "Название"








