from Space7.conftest import chrome
from Space7.Pages.cb1 import xpath1
from Space7.Pages.cb1 import Checkbox1


def test_ch1_1(chrome):
    run = Checkbox1(chrome)
    run.site(chrome)
    check_box_1 = chrome.find_element(*xpath1)
    assert check_box_1 is not None, "Element not found"

def test_ch1_2(chrome):
    run = Checkbox1(chrome)
    run.site(chrome)
    check_box_1 = chrome.find_element(*xpath1)
    assert check_box_1.is_displayed(), "Element is not visible"

def test_ch1_3(chrome):
    run = Checkbox1(chrome)
    run.site(chrome)
    check_box_1 = chrome.find_element(*xpath1)
    assert check_box_1.tag_name == "a", "Element is not a link"

def test_ch1_4(chrome):
    run = Checkbox1(chrome)
    run.site(chrome)
    check_box_1 = chrome.find_element(*xpath1)
    assert check_box_1.is_enabled(), "Element is not clickable"

def test_ch1_5(chrome):
    run = Checkbox1(chrome)
    run.site(chrome)
    check_box_1 = chrome.find_element(*xpath1)
    check_box_1.click()
    assert chrome.current_url == "https://www.qa-practice.com/elements/checkbox/single_checkbox", "URL did not change as expected"





