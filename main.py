from datetime import datetime
import pytz
import app

timezone = pytz.timezone('Asia/Jakarta')

current = datetime.time(datetime.now(timezone)).hour

if current >= 6 and current <= 7:
    # if datetime.weekday(datetime.now()) < 5:
    client = app.AbsenAutomation('https://bit.ly/presensiXIIgrf')
    client.start()
    # else:
    # exit()
else:
    exit()
