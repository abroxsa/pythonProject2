import time

from .locators import Product
class PageObject():
    def add_to_basket(self):
        self.browser.implicitly_wait(5)
        basket = self.browser.find_element(*Product.ADD_TO_BASKET)
        basket.click()