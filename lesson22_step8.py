import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')
browser.maximize_window()

first_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
first_name.send_keys('oxana')

last_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
last_name.send_keys('Abramova')

e_mail = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
e_mail.send_keys('adn@mail.com')

button = browser.find_element(By.XPATH, '//*[@id="file"]')



current_dir = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(current_dir, 'file.txt')
button.send_keys(file_path)

button2 = browser.find_element(By.XPATH, '/html/body/div[1]/form/button')
button2.click()





time.sleep(10)
browser.quit()