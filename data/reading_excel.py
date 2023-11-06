import xlrd

path1 = r"C:\Users\sujat\OneDrive\Desktop\webshopexcel.xlsx"
path = r"C:\Users\sujat\OneDrive\Desktop\New folder\webshopexcel.xlsx"

work_book = xlrd.open_workbook(path)
work_sheet = work_book.sheet_by_name("Sheet1")
rows_ = work_sheet.get_rows()
header = next(rows_)

def locator_data():
    d = {}
    for ele in rows_:
        d[ele[0].value] = (ele[1].value, ele[2].value)

    return d

print(locator_data())