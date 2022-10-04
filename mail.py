import win32com.client as win32
import pandas as pd
from datetime import datetime
import os

df = pd.read_excel("F:/Research/_Performing Credit Quantitative Research/R/Sharepoint/EarningsNote_check.xlsx")

# Open up an outlook email
outlook = win32.gencache.EnsureDispatch('Outlook.Application')
mail = outlook.CreateItem(0)

# Label the subject
#new_mail.Subject = "{:%m/%d} Report Update".format(date.today())

# Add the to and cc list
mail.To = 'aln@capital-four.com'
mail.Subject = 'Sample Email'
text = "Hi, this mail is written from Python."
mail.HTMLBody = "<body>" + text + "<p><p><p>" + "<body><br>" + \
                df.to_html() + \
                "<p><p><p>" + \
                "<br><i>" + datetime.now().strftime("%d-%m-%Y %H:%M:") + " This email was autogenerated" + " by: " + os.getlogin() + "</i><br>"
#mail.Body = "This is the normal body" + "\n \n \n" + \
#            datetime.now().strftime("%d-%m-%Y %H:%M:") + " This email was autogenerated" + " by: " + os.getlogin()
#mail.Attachments.Add('c:\\sample.xlsx')
#mail.Attachments.Add('c:\\sample2.xlsx')
#mail.CC = 'aln@capital-four.com'

mail.Send()