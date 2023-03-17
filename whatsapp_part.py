import pywhatkit
import datetime
import setting

def send_whatsApp(mail):
    now = datetime.datetime.now()
    try:
        pywhatkit.sendwhatmsg(setting.PHONE_NUMBER, time_hour=now.hour, time_min=now.minute+1, message=mail, tab_close=True)
    except Exception as ex:
        print(ex)