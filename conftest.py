import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help="Choose browser: chrome or firefox. Default: chrome."
    )
    parser.addoption(
        '--language',
        action='store',
        default='en-gb',
        help="Choose language, default: en-gb"
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    fmt = '\nstart {} browser with language "{}" for test..'
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        print(fmt.format(browser_name, language))
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
        print(fmt.format(browser_name, language))
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    browser.quit()
