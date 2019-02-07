import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('bdog.json', scope)
client = gspread.authorize(creds)

sheet = client.open('CMD').sheet1

mode = input("W/D? >")
if mode.lower() == 'd':
    start = 2
    while True:
        if sheet.cell(start, 1).value != '':
            sheet.update_cell(start, 1, '')
            start += 1
        else:
            quit()

else:
    with open('command.txt') as f:
        code = f.read().split('\n')

    for i, command in enumerate(code, 3):
        sheet.update_cell(i, 1, command)

    sheet.update_cell(2, 1, 'RUN')