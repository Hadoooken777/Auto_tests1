from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()


def test_open_s6(browser):
    browser.get('https://demoblaze.com/prod.html?idp_=1')


    galaxy_s6 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="Samsung galaxy s6"]'))
    )
    galaxy_s6.click()
    title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'h2'))
    )

    assert title.text == 'Samsung galaxy S6'