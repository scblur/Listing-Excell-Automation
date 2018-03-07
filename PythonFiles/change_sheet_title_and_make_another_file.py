import openpyxl
wb = openpyxl.load_workbook("basefile.xlsx")
print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name("Sheet1")
print(sheet.title)
sheet.title = "New Title"
print(wb.get_sheet_names())
wb.save("basefile2.xlsx")
