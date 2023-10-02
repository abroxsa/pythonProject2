from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    browser.maximize_window()

    box = browser.find_element(By.XPATH, '//*[@id="treasure"]')
    x = box.get_attribute('valuex')
    y = calc(x)


    answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer.send_keys(y)


    check_robot = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    check_robot.click()
    check = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    check.click()
    button = browser.find_element(By.XPATH, '/html/body/div/form/div/div/button')
    button.click()
finally:
    time.sleep(10)
    browser.quit()