'''Импорт библиотек'''

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.gov.spb.ru/')
driver.maximize_window()
time.sleep(5)

search_bar = driver.find_element(By.XPATH, '//*[@id="search_text"]')
search_bar.send_keys('бюджет Санкт-Петербурга')

button = driver.find_element(By.XPATH, '//*[@id="button-addon2"]')
button.click()
#
#
# login = driver.find_element(By.XPATH, '//*[@id="id_login_email"])
# search.send_keys('Git')
# search.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()