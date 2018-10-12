import allure
from selenium import webdriver
import pytest
from my_code.jira_requests import Jira_requests
from my_code.json_fixtures import Json_fixtures
import logging
from ui.tests_ui.test_issues_ui import Test_Issues_Page

use_api = Jira_requests()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    driver: webdriver = item.instance.driver
    if driver is not None:
        if rep.when in 'call' and rep.failed:
            allure.attach(driver.get_screenshot_as_png(),
                          name=item._pyfuncitem.name,
                          attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope="class")
def prepare_issue(request):
    id = []
    logging.info('\nCreating ticket via API...')
    response = use_api.create_ticket(Json_fixtures.create_ticket_json('API call from fixtures'))
    if response.status_code == 201:
        Test_Issues_Page.issue_key.append(response.json().get('key')[-5:])
        id.append(response.json().get('id'))
    else:
        logging.warning('Issue was not created via API')

    def clean_issue():
        logging.info('Making cleanup from fixtures...')
        result = use_api.delete_ticket(id[0])
        if result.status_code == 204:
            logging.info('Ticket with KEY ' + str(Test_Issues_Page.issue_key[0]) + ' and ID ' + id[0] + ' has been removed')
        else:
            logging.warning('Ticket ' + str(Test_Issues_Page.issue_key[0]) + 'has NOT been removed!!! ')

    request.addfinalizer(clean_issue)
