from .pages.main_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.test_go_to_login_page_from_main
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()                      
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.test_guest_see_login_link
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.test_cant_see_product_in_basket_from_main_page
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_busket()
    page.busket_should_be_empty()
    page.message_empty_busket_should_be()