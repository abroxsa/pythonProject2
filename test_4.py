import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
login_standard_user = 'standard_user'
password_all = 'secret_sauce'
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys('standard_user')
print('Input Login')
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('secret_sauce')
print('Input Password')
button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
button_login. click()
print('Click Login Button')

# driver.execute_script("window.scrollTo(0, 500)")
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
action. move_to_element(red_t_shirt).perform()
time.sleep(5)
driver.quit()