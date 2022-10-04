import win32com.client as win32

# Open an existing workbook
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open('workbook1.xlsx')
wb = excel.Workbooks.Open("F:/Research/_Performing Credit Quantitative Research/R/scores_to_sql/Analysis.xlsx")
wb.Save()
wb.Close()
excel.Visible = True
excel.Application.Quit()