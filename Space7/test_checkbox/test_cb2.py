import time
from selenium.webdriver.support.ui import Select
from Space7.conftest import chrome
from Space7.Pages.cb1 import Checkbox1
from Space7.Pages.cb2 import Checkbox2, xpath3, xpath4, xpath2, xpath5, xpath6, xpath7, xpath8, xpath9, xpath10



def test_ch2_1(chrome):
    run = Checkbox1(chrome)
    run.site(chrome)
    check_box_2 = chrome.find_element(*xpath2)
    assert check_box_2 is not None, "Element not found"


def test_ch2_2(chrome):
     run = Checkbox1(chrome)
     run.site(chrome)
     check_box_2 = chrome.find_element(*xpath2)
     assert check_box_2.is_displayed(), "Element is not visible"


def test_ch2_3(chrome):
    run = Checkbox1(chrome)
    run.site(chrome)
    check_box_2 = chrome.find_element(*xpath2)
    assert check_box_2.tag_name == "a", "Element is not a link"


def test_ch2_4(chrome):
    run = Checkbox1(chrome)
    run.site(chrome)
    check_box_2 = chrome.find_element(*xpath2)
    assert check_box_2.is_enabled(), "Element is not clickable"

#Баг
#def test_ch2_5(chrome):
 #   chrome.get("https://www.qa-practice.com/")
  #  check_box_2 = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Select input")))
   # check_box_2.click()
    #assert chrome.current_url == "https://www.qa-practice.com/elements/select/single_select", "URL did not change as expected"

def test_ch3_1(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    check_box_3 = chrome.find_element(*xpath3)
    assert check_box_3 is not None, "Element not found"

def test_ch3_2(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    check_box_3 = chrome.find_element(*xpath3)
    assert check_box_3.is_displayed(), "Element is not visible"

def test_ch3_3(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    check_box_3 = chrome.find_element(*xpath3)
    assert check_box_3.tag_name == "a", "Element is not a link"

def test_ch3_4(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    check_box_3 = chrome.find_element(*xpath3)
    assert check_box_3.is_enabled(), "Element is not clickable"

def test_ch4_1(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    check_box_4 = chrome.find_element(*xpath4)
    assert check_box_4 is not None, "Element not found"


def test_ch4_2(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    check_box_4 = chrome.find_element(*xpath4)
    assert check_box_4.is_displayed(), "Element is not visible"

def test_ch4_3(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    check_box_4 = chrome.find_element(*xpath4)
    assert check_box_4.tag_name == "a", "Element is not a link"


def test_ch4_4(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    check_box_4 = chrome.find_element(*xpath4)
    assert check_box_4.is_enabled(), "Element is not clickable"

def test_ch4_5(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    chrome.find_element(*xpath4)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/single_select", "URL did not change as expected"


def test_ch5_1(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Python")
    selected_option = select.first_selected_option
    assert selected_option.text == "Python", f"Expected 'Python', but got {selected_option.text}"


def test_ch5_2(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Ruby")
    selected_option = select.first_selected_option
    assert selected_option.text == "Ruby", f"Expected 'Ruby', but got {selected_option.text}"


def test_ch5_3(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("JavaScript")
    selected_option = select.first_selected_option
    assert selected_option.text == "JavaScript", f"Expected 'JavaScript', but got {selected_option.text}"


def test_ch5_4(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Java")
    selected_option = select.first_selected_option
    assert selected_option.text == "Java", f"Expected 'Java', but got {selected_option.text}"

def test_ch5_5(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("C#")
    selected_option = select.first_selected_option
    assert selected_option.text == "C#", f"Expected 'C#', but got {selected_option.text}"

def test_ch6_1_1(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Python")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    python = chrome.find_element(*xpath5)
    assert python is not None, "Element not found"

def test_ch6_1_2(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Python")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    python = chrome.find_element(*xpath5)
    assert python.is_displayed(), "Element is not visible"

def test_ch6_1_3(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Python")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    python = chrome.find_element(*xpath5)
    assert python.tag_name != "a", "Element is a link"


def test_ch6_1_4(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Python")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    chrome.find_element(*xpath5)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/single_select", "URL did not change as expected"


def test_ch6_2_1(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Ruby")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    ruby = chrome.find_element(*xpath5)
    assert ruby is not None, "Element not found"

def test_ch6_2_2(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Ruby")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    ruby = chrome.find_element(*xpath5)
    assert ruby.tag_name != "a", "Element is a link"

def test_ch6_2_3(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Ruby")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    ruby = chrome.find_element(*xpath5)
    assert ruby.tag_name != "a", "Element is a link"

def test_ch6_2_4(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Ruby")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    chrome.find_element(*xpath5)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/single_select", "URL did not change as expected"

def test_ch6_3_1(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("JavaScript")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    javascript = chrome.find_element(*xpath5)
    assert javascript is not None, "Element not found"

def test_ch6_3_2(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("JavaScript")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    javascript = chrome.find_element(*xpath5)
    assert javascript.tag_name != "a", "Element is a link"


def test_ch6_3_3(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("JavaScript")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    javascript = chrome.find_element(*xpath5)
    assert javascript.tag_name != "a", "Element is a link"

def test_ch6_3_4(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("JavaScript")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    chrome.find_element(*xpath5)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/single_select", "URL did not change as expected"


def test_ch6_4_1(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Java")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    java = chrome.find_element(*xpath5)
    assert java is not None, "Element not found"

def test_ch6_4_2(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Java")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    java = chrome.find_element(*xpath5)
    assert java.tag_name != "a", "Element is a link"

def test_ch6_4_3(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Java")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    java = chrome.find_element(*xpath5)
    assert java.tag_name != "a", "Element is a link"


def test_ch6_4_4(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("Java")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    chrome.find_element(*xpath5)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/single_select", "URL did not change as expected"

def test_ch6_5_1(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("C#")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    ci = chrome.find_element(*xpath5)
    assert ci is not None, "Element not found"

def test_ch6_5_2(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("C#")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    ci = chrome.find_element(*xpath5)
    assert ci.tag_name != "a", "Element is a link"

def test_ch6_5_3(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("C#")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    ci = chrome.find_element(*xpath5)
    assert ci.tag_name != "a", "Element is a link"


def test_ch6_5_4(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    dropdown = chrome.find_element(*xpath4)
    select = Select(dropdown)
    select.select_by_visible_text("C#")
    select.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    submit.click()
    chrome.find_element(*xpath5)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/single_select", "URL did not change as expected"






def test_ch6_6_1(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    chrome.find_element(*xpath6).click()
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL Error"

#Баг
#def test_ch6_6_2(chrome):
   # chrome.get("https://www.qa-practice.com/elements/select/mult_select")
  #  multiple = chrome.find_element(By.LINK_TEXT, "Multiple selects")
  #  multiple.click()
  #  assert multiple.is_displayed(), "Element is not visible"

#БАГ
#def test_ch6_6_3(chrome):
 #   chrome.get("https://www.qa-practice.com/elements/select/single_select")
  #  multiple = chrome.find_element(By.XPATH, "//a[contains(text(),'Multiple selects')]")
   # multiple.click()
    #assert multiple.tag_name == "a", "Element is not a link"


#БАГ
#def test_ch6_6_4(chrome):
 #   chrome.get("https://www.qa-practice.com/elements/select/single_select")
  #  multiple = chrome.find_element(By.XPATH, "//a[contains(text(),'Multiple selects')]").click()
   # assert multiple.is_enabled(), "Element is not clickable"

def test_ch6_6_5(chrome):
    run = Checkbox2(chrome)
    run.site2(chrome)
    chrome.find_element(*xpath6).click()
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL Error"





def test_ch6_7_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_7_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_7_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_7_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_8_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_8_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_8_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"


def test_ch6_8_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_9_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_9_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_9_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_9_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_10_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_10_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_10_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"


def test_ch6_10_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Sea")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"


def test_ch6_11_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_11_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_11_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_11_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_12_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_12_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_12_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_12_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_13_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_13_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_13_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_13_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"


def test_ch6_14_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_14_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_14_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_14_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Mountains")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_15_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_15_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"


def test_ch6_15_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_15_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_16_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_16_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_16_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_16_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_17_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_17_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_17_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_17_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"


def test_ch6_18_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_18_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_18_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_18_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Old town")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_19_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_19_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_19_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_19_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_20_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_20_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_20_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_20_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_21_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_21_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_21_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_21_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_22_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_22_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_22_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_22_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Ocean")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_23_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_23_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_23_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"


def test_ch6_23_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_24_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_24_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_24_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_24_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Car")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_25_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_25_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_25_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_25_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Bus")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Today")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_26_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_26_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_26_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_26_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Train")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Tomorrow")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"

def test_ch6_27_1(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.is_displayed(), "Element is not visible"

def test_ch6_27_2(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result is not None, "Element not found"

def test_ch6_27_3(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    result = chrome.find_element(*xpath10)
    assert result.tag_name != "a", "Element is a link"

def test_ch6_27_4(chrome):
    run = Checkbox2(chrome)
    run.site_mult(chrome)
    dropdown1 = chrome.find_element(*xpath7)
    select1 = Select(dropdown1)
    select1.select_by_visible_text("Restaurant")
    select1.first_selected_option.click()
    dropdown2 = chrome.find_element(*xpath8)
    select2 = Select(dropdown2)
    select2.select_by_visible_text("Air")
    select2.first_selected_option.click()
    dropdown3 = chrome.find_element(*xpath9)
    select3 = Select(dropdown3)
    select3.select_by_visible_text("Next week")
    select3.first_selected_option.click()
    submit = chrome.find_element(*xpath3)
    chrome.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(1)
    submit.click()
    chrome.find_element(*xpath10)
    assert chrome.current_url == "https://www.qa-practice.com/elements/select/mult_select", "URL did not change as expected"






































