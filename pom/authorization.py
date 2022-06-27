from base.base import BaseObject
from locators.locators import AuthorizationLocators as a, PageElementLocators as p

with open('file.txt') as f:
    password = f.read()


class AuthorizationSteps(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_correct_username(self):
        self.is_present('id', a.FIND_USERNAME_FIELD_ID).send_keys('standard_user')

    def enter_incorrect_username(self):
        self.is_present('id', a.FIND_USERNAME_FIELD_ID).send_keys('wrong_username')

    def enter_correct_password(self):
        self.is_present('id', a.FIND_PASSWORD_FIELD_ID).send_keys(f'{password}')

    def enter_incorrect_password(self):
        self.is_present('id', a.FIND_PASSWORD_FIELD_ID).send_keys('wrong_password')

    def click_to_login_button(self):
        self.is_present('id', a.FIND_LOGIN_BUTTON_ID).click()


class AuthorizationAsserts(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assertion_text_product_on_main_page(self):
        expected_text = 'PRODUCTS'
        actual_text = self.is_present('class', p.FIND_PRODUCTS_TEXT_ON_LOGGED_PAGE_CLASS).text
        assert expected_text == actual_text, f'Error. Expected text is {expected_text}, but actual text is {actual_text}'

    def assertion_text_if_wrong_credentials_are_entered(self):
        expected_text = 'Epic sadface: Username and password do not match any user in this service'
        actual_text = self.is_present('tag_name', a.FIND_WRONG_CREDENTIALS_ERROR_TEXT_TAG_NAME).text
        assert actual_text == expected_text, f'Error. Expected text is {expected_text}, but actual text is {actual_text}'

