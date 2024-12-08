from itertools import product

from selenium import webdriver

from selenium.webdriver.common.by import By
import pytest
import time
from Pages.homepage import HomePage
from Pages.product import ProductPage




@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')
    browser.close()


def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    #browser.get('https://demoblaze.com/index.html')
    homepage.click_monitor()
    #monitor_link = browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    #monitor_link.click()
    time.sleep(2)
    homepage.check_products_count(2)
    #monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    #assert len (monitors) == 2


