import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv

def run_automation(csv_file_path, profile_name):

    #Variables
    contact_numbers = []
    count = 0
    MESSAGES_URL = 'https://messages.google.com/web/conversations/new'
    PROFILE_DIR = profile_name
    USER_DATA_DIR = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Local\\Google\\Chrome\\User Data\\'
    chrome_driver_path = "chromedriver-win64\\chromedriver.exe"
    
    # Setting the path of the CONTACTS CSV file
    csv_path = csv_file_path.split('\\')
    csv_path = "\\\\".join(csv_path)

    # Extracting the first 100 contact number (Note to self : remove duplicates)
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if(count <= 100):
                count += 1
                contact_numbers.append(row[0])
            else:
                break

    #Tuning How Chrome opens
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir={}'.format(USER_DATA_DIR))
    options.add_argument('profile-directory={}'.format(PROFILE_DIR))


    #Running Chrome
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(MESSAGES_URL)
    
    time.sleep(5)

    button = driver.find_element(By.CSS_SELECTOR, 'button[data-e2e-start-group-chat-button]')
    button.click()

    input_field = driver.find_element(By.CSS_SELECTOR, 'input[data-e2e-contact-input]')

    for i in range(count):
        input_field.send_keys(contact_numbers[i] + Keys.RETURN)
        time.sleep(2)
        input_field.send_keys(Keys.ENTER)

    time.sleep(3600)
    
    # Quit the browser
    driver.quit()
