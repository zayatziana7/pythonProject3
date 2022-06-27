import pytest
from pom.authorization import AuthorizationSteps, AuthorizationAsserts
import allure

@allure.story('Authorization test cases')
@pytest.mark.usefixtures('setup')
class TestAuthorization:
    @pytest.mark.ui
    @allure.label("owner", "Yana") #метка для имени того кто создал тест кейс
    @allure.severity(allure.severity_level.BLOCKER) # метка для обозначения значимости тест кейса
    @allure.description('Checking successful logIn') # метка для названия тест кейа
    def test_successful_login(self):
        driver = self.driver
        authorization_steps = AuthorizationSteps(driver)
        authorization_asserts = AuthorizationAsserts(driver)
        with allure.step('Entering correct username'): # метка для названия шага
            authorization_steps.enter_correct_username()
        with allure.step('Entering correct password'):
            authorization_steps.enter_correct_password()
        with allure.step('Click to login button'):
            authorization_steps.click_to_login_button()
        with allure.step('Verify that login is successful'):
            authorization_asserts.assertion_text_product_on_main_page()

    @pytest.mark.ui
    @allure.label("owner", "Yana")  # метка для имени того кто создал тест кейс
    @allure.severity(allure.severity_level.BLOCKER)  # метка для обозначения значимости тест кейса
    @allure.description('Incorrect username')
    def test_unsuccessful_login_with_incorrect_username(self):
        driver = self.driver
        authorization_steps = AuthorizationSteps(driver)
        authorization_asserts = AuthorizationAsserts(driver)
        with allure.step('Entering an invalid username'):
            authorization_steps.enter_incorrect_username()
        with allure.step('Entering the correct password'):
            authorization_steps.enter_correct_password()
        with allure.step('Click on the login button'):
            authorization_steps.click_to_login_button()
        with allure.step('Make sure you entered the wrong username'):
            authorization_asserts.assertion_text_if_wrong_credentials_are_entered()

