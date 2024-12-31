


class BasePage:
    def __init__(self, chrome):
        self.chrome = chrome

    def find(self, args):
        return self.chrome.find_element(*args)


