# JSON file not included in project due to private details - however, code will work with another created Google API

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('PythonDB-json.json', scope)
client = gspread.authorize(creds)

sheet = client.open('PythonDB-sheet').sheet1

pp = pprint.PrettyPrinter()
result = sheet.get_all_records()
#result = sheet.row_values(1)
#result = sheet.col_values(1)
#result = sheet.cell(3,2)
pp.pprint(result)

#sheet.update_cell(3,2, 'Hello')
#result = sheet.cell(3,2).value
#pp.pprint(result)

#print(sheet.row_count)
#row = ["I'm", "updating", "this", "from", "Python!"]
#index = 3
#sheet.insert_row(row, index)
#print(sheet.row_count)
#sheet.delete_row(3)
#print(sheet.row_count)