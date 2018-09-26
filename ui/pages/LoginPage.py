from selenium.webdriver.common.by import By
from ui.Waits import Waits


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    login_URL = 'http://jira.hillel.it:8080/login.jsp'
    username_field = (By.CSS_SELECTOR, "input#login-form-username")
    password_field = (By.CSS_SELECTOR, "input#login-form-password")
    logIn_button = (By.CSS_SELECTOR, "input#login-form-submit")

    def doLogin(self, user, password):
        self.driver.get(self.login_URL)
        Waits.waitForElementIsVisible(self.driver, self.username_field).send_keys(user)
        self.driver.find_element(*self.password_field).send_keys(password)
        Waits.waitForElementIsClickable(self.driver, self.logIn_button).click()
        return self.driver.title

