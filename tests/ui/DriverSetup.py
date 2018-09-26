import os
import pytest
from selenium import webdriver


class DriverSetup:

    @pytest.yield_fixture(autouse=True)
    def init_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('start-maximized')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        chromedriver = dir_path + "/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(options=options, executable_path=chromedriver)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        yield  # everything after 'yield' is executed on tear-down

        if (self.driver != None):
            self.driver.close()
            self.driver.quit()
