
from selenium.webdriver.common.by import By
from Space7.Pages.base_page import BasePage
from Space7.conftest import chrome


xpath2 = (By.XPATH, "//a[contains(text(),'Select input')]")
xpath3 = (By.XPATH, "//input[@id='submit-id-submit']")
xpath4 = (By.XPATH, "//select[@id='id_choose_language']")
xpath5 = (By.XPATH, "//div[@id='result']")
xpath6 = (By.XPATH, "//a[contains(text(),'Multiple selects')]")
xpath7 = (By.XPATH, "//select[@id='id_choose_the_place_you_want_to_go']")
xpath8 = (By.XPATH, "//select[@id='id_choose_how_you_want_to_get_there']")
xpath9 = (By.XPATH, "//select[@id='id_choose_when_you_want_to_go']")
xpath10 = (By.XPATH, "//p[@id='result-text']")

class Checkbox2(BasePage):
    def __init__(self, chrome):
        super().__init__(chrome)

    def by_xpath(self):
        return self.find(*xpath2)

    def site2(self, chrome):
        self.chrome.get("https://www.qa-practice.com/elements/select/single_select")

    def site_mult(self, chrome):
        self.chrome.get("https://www.qa-practice.com/elements/select/mult_select")

    def by_xpath2(self):
        return self.find(*xpath3)

    def by_xpath3(self):
        return self.find(*xpath4)

    def by_xpath4(self):
        return self.find(*xpath5)

    def by_xpath5(self):
        return self.find(*xpath6)

    def by_xpath6(self):
        return self.find(*xpath7)

    def by_xpath7(self):
        return self.find(*xpath8)

    def by_xpath8(self):
        return self.find(*xpath9)

    def by_xpath9(self):
        return self.find(*xpath10)



