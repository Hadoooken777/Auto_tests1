
from Space7.conftest import chrome
from selenium.webdriver.common.by import By
from Space7.Pages.base_page import BasePage

xpath1 = (By.XPATH, "//a[contains(text(),'Single checkbox')]")


class Checkbox1(BasePage):
    def __init__(self,chrome):
        super().__init__(chrome)

    def by_xpath(self):
        return self.find(xpath1)

    def site(self, chrome):
        self.chrome.get('https://www.qa-practice.com/')





