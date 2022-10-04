import win32com.client as win32

# Open an existing workbook
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open('workbook1.xlsx')
wb = excel.Workbooks.Open("C:/workbook1.xlsx")
wb.Save()
wb.Close()
excel.Visible = True
excel.Application.Quit()
