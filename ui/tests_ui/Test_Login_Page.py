from ui.pages.LoginPage import LoginPage
from ui.DriverSetup import DriverSetup
import unittest
import pytest
import logging


class Test_Login_Page(DriverSetup):
    User = 'Evgeniy_Shchelkunov'
    Password = 'Password1@'
    Wrong_user = 'Evgeniy'
    Wrong_password = 'pass11211'
    failed_login = 'Log in - Hillel IT School JIRA'
    successful_login = 'System Dashboard - Hillel IT School JIRA'

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()

    test_data = [
        (User, Wrong_password, failed_login),
        (Wrong_user, Password, failed_login),
        (User, Password, successful_login),
    ]

    @pytest.mark.parametrize("user, password, result", test_data)
    def test_first(self, user, password, result):
        logging.info('\nTesting login with user: ' + user + ' password: ' + password)
        login_page = LoginPage(self.driver)
        result = login_page.doLogin(user, password, result)
        assert result is True


if __name__ == "__main__":
    unittest.main()
