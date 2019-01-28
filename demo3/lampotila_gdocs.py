import lampotila
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('google_creds.json', scope)
gc = gspread.authorize(credentials)
sh = gc.open("tiea345-temps")
worksheet = sh.sheet1
# Käytin tätä aluksi taulukon tyhjentämiseen.
# worksheet.resize(1)

while True:
    try:
        humidity, temp = lampotila.get_temp()
        print(humidity, temp)
        worksheet.append_row([str(temp), str(humidity), str(datetime.datetime.now())])
    except KeyboardInterrupt:
        print("Stopping")
