'''Импорт библиотек'''
import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver.common.by import By # Импортируем библиотеку By

driver = webdriver.Chrome()
driver.get('https://stepik.org/lesson/236895/step/1')
driver.maximize_window()
driver.implicitly_wait(15)

login = driver.find_element(By.XPATH, '//*[@id="ember33"]')
login.click()

user_name = driver.find_element(By.XPATH,'//*[@id="id_login_email"]')
user_name.send_keys('regressor1@gmail.com')

password = driver.find_element(By.XPATH, '//*[@id="id_login_password"]')
password.send_keys('ksjdk')

button = driver.find_element(By.XPATH, '//*[@id="login_form"]/button')
button.click()

time.sleep(10)
driver.close()