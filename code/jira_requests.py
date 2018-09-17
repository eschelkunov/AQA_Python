import requests


class Jira_requests:

    loginURL = 'http://jira.hillel.it:8080/rest/auth/1/session'
    createIssueURL = 'http://jira.hillel.it:8080/rest/api/2/issue/'
    searchIssueURL = 'http://jira.hillel.it:8080/rest/api/2/search?jql='
    auth = ('Evgeniy_shchelkunov', 'Password1@')

    header = {'Content-Type': 'application/json'}

    def login_to_jira(self, username, password):
        response = requests.get(self.loginURL, auth=(username, password))
        return response.status_code

    def create_ticket(self, json_data):
        response = requests.post(self.createIssueURL, headers=self.header, data=json_data, auth=self.auth)
        return response

    def search_for_ticket(self, key):
        response = requests.get(self.searchIssueURL+str(key), auth=self.auth)
        return response

    def update_ticket(self, key, json_data):
        response = requests.put(self.createIssueURL+str(key), headers=self.header, data=json_data, auth=self.auth)
        return response

    def delete_ticket(self, key):
        response = requests.delete(self.createIssueURL + str(key), auth=self.auth)
        return response.status_code
