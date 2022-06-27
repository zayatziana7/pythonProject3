from base.base import BaseObject
from locators.locators import Button as a, PageElementLocators as p, Button as t



class AddButton(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_button(self):
        self.is_present('id', a.FIND_ADD).send_keys('add-to-cart-sauce-labs-backpack')

    def click_to_add(self):
        self.is_present('id', a.FIND_ADD).click()

    def enter_basket(self):
        self.is_clickable('class', a.FIND_BASKET)

    def click_to_basket(self):
        self.is_clickable('class', a.FIND_BASKET).click()

    def enter_selector(self):
        self.is_clickable('id', a.FIND_SELECTOR)

    def click_to_selector(self):
        self.is_clickable('id', a.FIND_SELECTOR).click()

    def enter_remove(self):
        self.is_clickable('id', a.FIND_REMOVE)

    def click_to_remove(self):
        self.is_clickable('id', a.FIND_REMOVE).click()



class ButtonAsserts(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assertion_buttonAsserts(self):
        expected_text = 'PRODUCTS'
        actual_text = self.is_present('class', p.FIND_PRODUCTS_TEXT_ON_LOGGED_PAGE_CLASS).text
        assert expected_text == actual_text, f'Error. Expected text is {expected_text}, but actual text is {actual_text}'

    def assertion_cart(self):
        expected_text = 'YOUR CART'
        actual_text = self.is_present('css', t.FIND_CART).text
        assert expected_text == actual_text, f'Error. Expected text is {expected_text}, but actual text is {actual_text}'