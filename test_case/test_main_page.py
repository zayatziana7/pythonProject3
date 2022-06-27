import pytest
from pom.authorization import AuthorizationSteps
from pom.main_page import AddButton, ButtonAsserts
import allure



@allure.story('MainPage test cases')
@pytest.mark.usefixtures('setup')
class TestMainPage:

    @pytest.mark.ui
    @allure.label("owner", "Yana")  # метка для имени того кто создал тест кейс
    @allure.severity(allure.severity_level.BLOCKER)  # метка для обозначения значимости тест кейса
    @allure.description('Add item to cart')
    def test_add_button(self):
        driver = self.driver
        authorization_steps = AuthorizationSteps(driver)
        add_buttons = AddButton(driver)
        button_asserts = ButtonAsserts(driver)
        with allure.step('Enter correct username'):
            authorization_steps.enter_correct_username()
        with allure.step('Enter_correct_password'):
            authorization_steps.enter_correct_password()
        with allure.step('Click to login button'):
            authorization_steps.click_to_login_button()
        with allure.step('Select product'):
            button_asserts.assertion_buttonAsserts()
        with allure.step('Push button ADD'):
            add_buttons.add_button()
        with allure.step('Add to Basket'):
            add_buttons.click_to_add()

    @pytest.mark.ui
    @allure.label("owner", "Yana")  # метка для имени того кто создал тест кейс
    @allure.severity(allure.severity_level.BLOCKER)  # метка для обозначения значимости тест кейса
    @allure.description('Saving an item to the cart')
    def test_basket_button(self):
        driver = self.driver
        authorization_steps = AuthorizationSteps(driver)
        add_buttons = AddButton(driver)
        button_asserts = ButtonAsserts(driver)
        with allure.step('Enter correct username'):
            authorization_steps.enter_correct_username()
        with allure.step('Enter_correct_password'):
            authorization_steps.enter_correct_password()
        with allure.step('Click to login button'):
            authorization_steps.click_to_login_button()
        with allure.step('Select product'):
            button_asserts.assertion_buttonAsserts()
        with allure.step('Push button ADD'):
            add_buttons.add_button()
        with allure.step('Add to Basket'):
            add_buttons.click_to_add()
        with allure.step('Enter basket'):
            add_buttons.enter_basket()
        with allure.step('Exit cart'):
            add_buttons.click_to_basket()

    @pytest.mark.ui
    @allure.label("owner", "Yana")  # метка для имени того кто создал тест кейс
    @allure.severity(allure.severity_level.BLOCKER)  # метка для обозначения значимости тест кейса
    @allure.description('Open cart')
    def test_selector_button(self):
        driver = self.driver
        authorization_steps = AuthorizationSteps(driver)
        add_buttons = AddButton(driver)
        button_asserts = ButtonAsserts(driver)
        with allure.step('Enter correct username'):
            authorization_steps.enter_correct_username()
        with allure.step('Enter_correct_password'):
            authorization_steps.enter_correct_password()
        with allure.step('Click to login button'):
            authorization_steps.click_to_login_button()
        with allure.step('Select product'):
            button_asserts.assertion_buttonAsserts()
        with allure.step('Enter selector'):
            add_buttons.enter_selector()
        with allure.step('Click selector'):
            add_buttons.click_to_selector()


    @pytest.mark.ui
    @allure.label("owner", "Yana")  # метка для имени того кто создал тест кейс
    @allure.severity(allure.severity_level.BLOCKER)  # метка для обозначения значимости тест кейса
    @allure.description('Incorrect username')
    def test_remove_from_cart(self):
        driver = self.driver
        authorization_steps = AuthorizationSteps(driver)
        add_buttons = AddButton(driver)
        button_asserts = ButtonAsserts(driver)
        with allure.step('Enter correct username'):
            authorization_steps.enter_correct_username()
        with allure.step('Enter_correct_password'):
            authorization_steps.enter_correct_password()
        with allure.step('Click to login button'):
            authorization_steps.click_to_login_button()
        with allure.step('Select product'):
            button_asserts.assertion_buttonAsserts()
        with allure.step('Push button ADD'):
            add_buttons.add_button()
        with allure.step('Add to Basket'):
            add_buttons.click_to_add()
        with allure.step('Enter basket'):
            add_buttons.enter_basket()
        with allure.step('Exit cart'):
            add_buttons.click_to_basket()
        with allure.step('Assertion cart'):
            button_asserts.assertion_cart()
        with allure.step('Enter remove'):
            add_buttons.enter_remove()
        with allure.step('Click remove'):
            add_buttons.click_to_remove()











