import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')
browser.maximize_window()

x = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x.text
y = str(math.log(abs(12*math.sin(int(x)))))
browser.execute_script("window.scrollBy(0, 100);")
answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
answer.send_keys(y)


button_robot = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
button_robot.click()
button_rool = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
button_rool.click()

submit = browser.find_element(By.XPATH, '/html/body/div/form/button')
submit.click()





time.sleep(10)
browser.quit()