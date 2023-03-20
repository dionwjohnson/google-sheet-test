from oauth2client.service_account import ServiceAccountCredentials
import gspread
# import json


"""
From: https://www.makeuseof.com/tag/read-write-google-sheets-python/
"""

# Python file for working with Google Sheets
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
# access the json key you downloaded earlier
credentials = ServiceAccountCredentials.from_json_keyfile_name("my_google_info.json", scopes)
file = gspread.authorize(credentials)  # authenticate the JSON key with gspread
sheet = file.open("Test_with_Python")  # open sheet
# sheet = sheet.number_one #replace sheet_name with the name that corresponds to yours,
# e.g, it can be sheet1

# replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
sheet = sheet.sheet1
all_cells = sheet.range('A1:A6')
print(all_cells)
print("-" * 22)
for cell in all_cells:
    print(cell.value)

sheet.update_acell('C2', 'Blue')
sheet.update_cell(2, 3, 'Blue') #updates row 2 on column 3
