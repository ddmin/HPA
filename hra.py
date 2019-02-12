import pyautogui
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('bdog.json', scope)
client = gspread.authorize(creds)

sheet = client.open('CMD').sheet1

CURRENT_COL = sheet.cell(1, 1).value

if CURRENT_COL == '':
    CURRENT_COL = 1
else:
    CURRENT_COL = int(CURRENT_COL)

sheet.update_cell(1, 1, CURRENT_COL + 1)

while True:
    try:
        time.sleep(1)
        if sheet.cell(2, CURRENT_COL).value == 'RUN':
            sheet.update_cell(2, CURRENT_COL, '')
            celli = 3
            while True:
                command = sheet.cell(celli, CURRENT_COL).value

                if command == 'CLOSE':
                    pyautogui.hotkey('alt', 'f4')
                elif command.startswith('MOVE'):
                    _, x, y = command.split()
                    pyautogui.moveTo(int(x), int(y))
                elif command == 'CLICK':
                    pyautogui.click()
                elif command == 'HOME':
                    pyautogui.hotkey('win', 'd')
                elif command == 'WIN':
                    pyautogui.press('win')
                elif command.startswith('TYPE'):
                    _, phrase = command.split()
                    pyautogui.typewrite(phrase)
                elif command.startswith('WAIT'):
                    _, sec = command.split()
                    time.sleep(int(sec))
                elif command == 'ENTER':
                    pyautogui.press('enter')
                elif command == 'SPACE':
                    pyautogui.press('space')
                elif command.startswith('CTRL'):
                    _, key = command.split()
                    pyautogui.hotkey('ctrl', key)
                elif command == 'EOF':
                    break
                else:
                    break

                celli += 1
    except:
        pass