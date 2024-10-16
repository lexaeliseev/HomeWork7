from pypdf import PdfReader
from zipfile import ZipFile
from conftest import TMP_DIR
from xlrd2 import open_workbook

# def test_check_pdf(create_zip_file):
#     with ZipFile(f"{TMP_DIR}/archive.zip") as zip_file:
#         print(zip_file.namelist())
#         with zip_file.open("pdf_file.pdf") as pdf_file:
#             reader = PdfReader(pdf_file)
#             assert len(reader.pages) == 1
#
#             check_text = reader.pages[0].extract_text().strip()
#             print(check_text)
#             # assert "Hello,World" in check_text


def test_check_xls(create_zip_file):
    with ZipFile(f"{TMP_DIR}/archive.zip") as zip_file:
        print(zip_file.namelist())
        with zip_file.open("import_ou_xls.xls") as xls_file:
            workbook = open_workbook(xls_file)
            sheet = workbook.active
            # print(len(sheet))


