from datetime import datetime
import pytz
from app import AbsenAutomation

timezone = pytz.timezone('Asia/Jakarta')

current = datetime.time(datetime.now(timezone)).hour

if current >= 6 and current <= 7:
    # if datetime.weekday(datetime.now()) < 5:
    client = AbsenAutomation('https://bit.ly/presensiXIIgrf')
    client.start()
    # else:
    # exit()
else:
    exit()
