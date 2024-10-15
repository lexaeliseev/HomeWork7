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