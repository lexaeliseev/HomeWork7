from pypdf import PdfReader

reader = PdfReader("download_file/Smoke.pdf")

print(reader.pages)  # список объектов страниц

print(len(reader.pages))  # количество страниц в файле

print(reader.pages[0].extract_text())  # печатает содержимое страницы
