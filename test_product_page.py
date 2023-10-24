from .pages.main_page import MainPage
from .pages.base_page import PageObject


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page = PageObject(browser, link)
    page.open()
    page.add_to_basket()
