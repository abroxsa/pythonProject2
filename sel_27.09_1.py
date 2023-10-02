import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://qase.io/')
driver.maximize_window()

login = driver.find_element(By.XPATH, '//*[@id="signin"]')
login.click()

user_name = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/section[2]/form/div[1]/div/input')
user_name.send_keys('acd@gmail.com')
password = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/section[2]/form/div[2]/div/input')
password.send_keys('1234')
time.sleep(5)
button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/section[2]/form/button/span')
button.click()
time.sleep(5)
driver.close()