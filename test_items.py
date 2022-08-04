from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def check_basket_button_existence(browser):
    browser.get(link)
    time.sleep(10)
    try:
        basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    except NoSuchElementException:
        return False
    return True


def test_basket_button_existence(browser):
    button_exists = check_basket_button_existence(browser)
    assert button_exists, "Button 'Add to basket' doesn't exist!"