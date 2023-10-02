'''Импорт библиотек'''

import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By # Импортируем библиотеку By

driver = webdriver.Chrome()
driver.get('https://stepik.org/catalog')
driver.maximize_window()
time.sleep(5)
login = driver.find_element(By.XPATH, '//*[@id="ember245"]')
login.click()

time.sleep(5)
user_name = driver.find_element(By.XPATH, '//*[@id="id_login_email"]')
user_name.send_keys('abroxsa@gmile.com')

password = driver.find_element(By.XPATH, '//*[@id="id_login_password"]')
password.send_keys('144000')

button = driver.find_element(By.XPATH, '//*[@id="login_form"]/button')
button.click()
#
#
# login = driver.find_element(By.XPATH, '//*[@id="id_login_email"])
# search.send_keys('Git')
# search.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()