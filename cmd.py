import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('.bdog.json', scope)
client = gspread.authorize(creds)
sheet = client.open('CMD').sheet1

print(
print('Cell- ExceLang Command Prompt v1.7')
print('Type "help" for more information.')

while True:
    cmd = input(">>> ")

    if cmd.lower().startswith('exit'):
        break

    elif cmd.lower().startswith("write"):
        splitted = cmd.split()

        comp = splitted[1]
        cmd = ' '.join(splitted[2:])

        sheet.update_cell(3, int(comp), cmd)
        sheet.update_cell(4, int(comp), "EOF") 
        sheet.update_cell(2, int(comp), "RUN")

    elif cmd.lower().startswith('ping'):
        print()
        _, comp = cmd.split()

        run = sheet.cell(2, int(comp)).value
        if run.startswith("RUN"):
            print(f"CPU {comp}\n<Response 404>")
        else:
            print(f"CPU {comp}\n<Response 200>")

        print()
    elif cmd.lower().startswith('howmany'):
        print()
        n = sheet.cell(1,1).value
        if n == '':
            number = 0
        else:
            number = int(n) - 1
        print(f'Number of computers: {number}')

        print()
    elif cmd.lower().startswith('post'):
        _, computer, content = cmd.split()

        computer = int(computer)

        file_name = os.path.join("src",content+".txt")

        try:          
            with open(file_name) as f:
                code = f.read().split('\n')

        except:
            print("\nInvalid Script.\n")
            continue

        for i, command in enumerate(code, 3):
            sheet.update_cell(i, computer, command)

        sheet.update_cell(2, computer, 'RUN')

    elif cmd.lower().startswith('scripts'):
        print()
        for script in os.listdir('./src'):
            print(script)

        print()
    elif cmd.lower().startswith('help'):
        print()
        print('PING <CPU>')
        
        print('POST <CPU> <FILENAME>')
        
        print('WRITE <CPU> <CMD>')
        print('HOWMANY')
        
        print('SCRIPTS')
        
        print('EXIT')
        print()
    
    else:
        print()
        print(f'{cmd} is not a valid command.')
        print()
