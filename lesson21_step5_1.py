from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')
    browser.maximize_window()

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)


    answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer.send_keys(y)


    check_robot = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/label')
    check_robot.click()
    check = browser.find_element(By.XPATH, '/html/body/div/form/div[4]/label')
    check.click()
    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()
finally:
    time.sleep(10)
    browser.quit()