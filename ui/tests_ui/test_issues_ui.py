import allure

from ui.pages.LoginPage import LoginPage
from ui.pages.IssuePage import IssuesPage
from ui.DriverSetup import DriverSetup
import unittest
import pytest
import logging


@pytest.mark.usefixtures('prepare_issue')
@allure.story('UI Issue tests')
class Test_Issues_Page(DriverSetup):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()

    credentials = ('Evgeniy_Shchelkunov', 'Password1@')
    test_data_create_ticket = [('', False), ('TooLongSummary' * 100, False), ('EugeneTestUI', True)]
    test_data_search_ticket = [('my_ticket', True), ('unknown', False)]
    test_data_update_ticket = [('summary', True), ('priority', True), ('assignee', True)]
    issue_key = []

    @unittest.skip('Skipped due to API is used to prepare ticket')
    @allure.step
    @allure.title('create ticket UI')
    @pytest.mark.parametrize("summary, expected_result", test_data_create_ticket)
    def test_create_ticket(self, summary, expected_result):
        logging.info('\nCreating ticket with Summary: ' + summary)
        LoginPage(self.driver).doLogin(*self.credentials)
        result = IssuesPage(self.driver).create_ticket(summary)
        assert expected_result == result

    @allure.step
    @allure.title('search for ticket UI')
    @pytest.mark.parametrize("ticket, expected_result", test_data_search_ticket)
    def test_search_for_ticket(self, ticket, expected_result):
        logging.info('\nSearching for ticket: ' + str(ticket))
        LoginPage(self.driver).doLogin(*self.credentials)
        result = IssuesPage(self.driver).search_for_ticket(ticket, self.issue_key[0])
        assert expected_result == result

    @allure.step
    @allure.title('search for few tickets UI')
    def test_search_for_few_tickets(self):
        logging.info('\nSearching for few tickets reported by me...')
        LoginPage(self.driver).doLogin(*self.credentials)
        assert IssuesPage(self.driver).search_for_few_ticket() >= 5

    @allure.step
    @allure.title('update ticket UI')
    @pytest.mark.parametrize("goal, expected_result", test_data_update_ticket)
    def test_update_tickets(self, goal, expected_result):
        logging.info('\nUpdating ticket\'s ' + goal)
        LoginPage(self.driver).doLogin(*self.credentials)
        assert IssuesPage(self.driver).update_ticket(goal) is expected_result

    @unittest.skip('Skipped due to API cleanup is used')
    @allure.step
    @allure.title('delete ticket UI')
    def test_delete_ticket(self):
        logging.info('Deleting the ticket....')
        LoginPage(self.driver).doLogin(*self.credentials)
        assert IssuesPage(self.driver).delete_ticket() is True


if __name__ == "__main__":
    unittest.main()
