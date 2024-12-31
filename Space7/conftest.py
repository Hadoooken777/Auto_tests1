import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()

def chrome():
    options = Options()
    options.add_argument("--headless")
    chrome = webdriver.Chrome(options=options)
    chrome.maximize_window()
    chrome.implicitly_wait(1)
    yield chrome
    chrome.quit()


