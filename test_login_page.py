from ..pages.login_page import LoginPage
import pytest


@pytest.mark.test_be_login_url
def test_guest_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()