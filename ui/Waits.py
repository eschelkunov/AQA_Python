from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Waits:

    @staticmethod
    def elementIsPresent(driver, element):
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located(element))
            return True
        except TimeoutException:
            return False

    @staticmethod
    def waitForElementIsVisible(driver, element):
        return WebDriverWait(driver, 5).until(EC.visibility_of_element_located(element))

    @staticmethod
    def waitForElementIsClickable(driver, element):
        return WebDriverWait(driver, 5).until(EC.element_to_be_clickable(element))

    @staticmethod
    def waitForElementsArePresent(driver, element):
        return WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(element))

