import platform
import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverSetup:

    @pytest.yield_fixture(autouse=True)
    def init_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('start-maximized')
        if platform.system() == "Darwin":
            dir_path = os.path.dirname(os.path.realpath(__file__))
            chromedriver = dir_path + "/webdrivers/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver = webdriver.Chrome(options=options, executable_path=chromedriver)
        else:
            self.driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        yield
        if (self.driver != None):
            self.driver.close()
            self.driver.quit()
