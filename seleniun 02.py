from selenium import webdriver
from selenium.webdriver.common.by import By
import time

    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    user_name.send_keys('standard_user')

    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys('secret_sauce')

   login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
   login_button.click()
   button_add_backpack = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')





    time.sleep(3)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


