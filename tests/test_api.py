import pytest
from random import randint
from code.jira_requests import Jira_requests
from code.json_fixtures import *
import logging

request = Jira_requests()


class Test_API:

    User = 'Evgeniy_Shchelkunov'
    Password = 'Password1@'
    Wrong_user = 'Evgeniy'
    Wrong_password = 'pass112233'
    issueID = []

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()

    def get_id(self):
        if len(self.issueID) > 0:
            return self.issueID[0]

    def set_id(self, id):
        self.issueID.append(id)

    @pytest.mark.parametrize("user, password, code", [
        (User, Password, 200),
        (User, Wrong_password, 401),
        (Wrong_user, Password, 401),
    ])
    def test_login(self, user, password, code):
        logging.info('Testing login to Jira with: ' + user + ' : ' + password)
        assert code == request.login_to_jira(user, password)

    @pytest.mark.parametrize("summary, code", [
        ('EvgeniyTest', 201),
        ('', 400),
        ('Summury' * 100, 400),
    ])
    def test_create_ticket(self, summary, code):
        logging.info('Testing creation of the issue with summary: ' + summary)
        response = request.create_ticket(Json_fixtures.create_ticket_json(summary))
        if response.status_code == 201:
            self.set_id(response.json().get('id'))
        assert code == response.status_code

    def test_search_for_ticket(self):
        logging.info('Searching for the issue with id: ' + self.get_id())
        response = request.search_for_ticket('id=' + self.get_id())
        assert 200 == response.status_code

    def test_search_for_unexisting_ticket(self):
        logging.info('Searching for unexisting issue...')
        response = request.search_for_ticket('id=' + str(randint(0, 9)*1000))
        assert 400 == response.status_code

    def test_search_for_few_tickets(self):
        logging.info('Searching for few issues and validation count is more or equals 5...')
        response = request.search_for_ticket('reporter=' + self.User)
        count = len(response.json().get("issues"))
        assert count >= 2

    @pytest.mark.parametrize("field, new_value", [
        ('summary', 'Updated summary'),
        ('description', 'Updated description..')
    ])
    def test_update_ticket_fields(self, field, new_value):
        logging.info('Updating field ' + field + ' with the new value: ' + new_value)
        response = request.update_ticket(self.get_id(), Json_fixtures.update_ticket_json(field, new_value))
        assert 204 == response.status_code

    @pytest.mark.parametrize("new_value", ['High', 'Highest'])
    def test_update_priority(self, new_value):
        logging.info('Changing priority to: ' + new_value)
        response = request.update_ticket(self.get_id(), Json_fixtures.update_priority_json(new_value))
        assert 204 == response.status_code

    def teardown_class(self):
        logging.info('Making cleanUp....')
        response = request.delete_ticket(self.get_id(self))
        logging.info('Ticket ' + str(self.get_id()) + 'has been removed!') if response == 204 else \
            logging.warning('Ticket could not be removed !')

    @pytest.mark.flaky(reruns=2)
    def test_example(self):
        logging.info('Getting rundom number...')
        num = randint(1, 2)
        logging.info('Rundom number is ' + str(num))
        assert 2 == num







