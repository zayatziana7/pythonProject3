from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class BaseObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def __selenium_by(self, find_by):
        selectors_dict = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'id': By.ID,
                    'name': By.NAME,
                    'class': By.CLASS_NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'link_text': By.LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return selectors_dict[find_by]

    def is_visible(self, find_by, locator):
        self.wait.until(ec.visibility_of_element_located((self.__selenium_by(find_by), locator)))

    def is_present(self, find_by, locator):
        return self.wait.until(ec.presence_of_element_located((self.__selenium_by(find_by), locator)))

    def is_not_visible(self, find_by, locator):
        return self.wait.until(ec.invisibility_of_element_located((self.__selenium_by(find_by), locator)))

    def is_clickable(self, find_by, locator):
        return self.wait.until(ec.element_to_be_clickable((self.__selenium_by(find_by), locator)))

    def are_visible(self, find_by, locator, locator_name) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located((self.__selenium_by(find_by), locator)),
                               locator_name)


