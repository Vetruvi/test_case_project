import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: Russian = ru, English = en, Espanol = es, French = fr")
    
    parser.addoption('--time_sleep', action='store', default=30,
                     help="How long to wait")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("language")

    options_chrome = Options()
    option_firefox = OptionsFirefox()

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        option_firefox.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=option_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def sleep(request):
    time_sleep = request.config.getoption("time_sleep")
    return int(time_sleep)