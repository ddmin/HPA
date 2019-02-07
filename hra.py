import pyautogui
import gspread
from oauth2client.service_account import ServiceAccountCredentials

WIDTH, HEIGHT = pyautogui.size()

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('bdog.json', scope)
client = gspread.authorize(creds)

sheet = client.open('CMD').sheet1

while True:
    try:
        pass
    except:
        pass

    break



# pyautogui.moveTo(X, Y)