from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from whatsapp_part import send_whatsApp


url = "https://messages.google.com/web/conversations"
driver = webdriver.Chrome(executable_path="/home/ivan/Documents/whatsapp_resender/chromedriver/chromedriver")


try:
    driver.get(url=url)
    time.sleep(30)
    last_message = ''
    while True:
        messages = driver.find_elements(By.TAG_NAME, "mws-conversation-list-item")
        new_last_message = messages[0].text.split('\n')[1]

        if new_last_message != last_message:
            last_message = new_last_message
            print(last_message)
            send_whatsApp(last_message)

        time.sleep(5)
except Exception as ex:
    print(f'{ex}..!!!!!!!!!!!!!!!!!!!!!!!!!!')
    

finally:
    driver.close()
    driver.quit()