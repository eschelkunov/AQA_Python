from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ui.Waits import Waits
from random import randint


class IssuesPage(object):

    def __init__(self, driver):
        self.driver = driver

    updated_summary = 'UpdatedSummaryUI'
    search = (By.CSS_SELECTOR, "input.search")
    issues_button = (By.CSS_SELECTOR, "a#find_link")
    create_button = (By.CSS_SELECTOR, "a#create_link")
    input_summary = (By.CSS_SELECTOR, "input#summary")
    submit_button = (By.CSS_SELECTOR, "input#create-issue-submit")
    priority_field = (By.CSS_SELECTOR, "input#priority-field")
    more_button = (By.CSS_SELECTOR, "a#opsbar-operations_more")
    delete_issue = (By.CSS_SELECTOR, "a#delete-issue")
    delete_issue_submit = (By.CSS_SELECTOR, "input#delete-issue-submit")
    assign_to_me = (By.CSS_SELECTOR, "#assign-to-me-trigger")
    edit_issue_button = (By.CSS_SELECTOR, "a#edit-issue")
    update_issue_button = (By.CSS_SELECTOR, ".button[name='Edit']")
    reported_by_me_button = (By.CSS_SELECTOR, "a#filter_lnk_reported_lnk")
    blocker = (By.XPATH, "//*[contains(@title,'Low')]")
    assignee = (By.XPATH, "#assignee-val>span[contains(@rel,'Evgeniy')]")
    my_issue = (By.XPATH, "//li[@title][contains(@data-key,'AQAPYTHON')]")
    ticket_id = (By.XPATH, "//a[contains(@class,'issue-created-key')][@data-issue-key]")
    summary_value = (By.XPATH, "//h1[@id='summary-val'][text()='" + updated_summary + "']")
    success_message = (By.XPATH, "//div[contains(@class,'success closeable shadowed')]")
    search_validation_point = (By.XPATH, "//a[contains(@data-issue-key,'AQAPYTHON-')]")
    ticket_is_deleted = (By.XPATH, "//div[contains(text(),'has been deleted')]")
    ticket_is_updated = (By.XPATH, "//div[contains(text(),'has been updated')]")
    issue_key = []

    def create_ticket(self, summary):
        Waits.waitForElementIsVisible(self.driver, self.create_button).click()
        self.driver.find_element(*self.input_summary).send_keys(summary)
        Waits.waitForElementIsClickable(self.driver, self.submit_button).click()
        if Waits.elementIsPresent(self.driver, self.success_message) is True:
            self.issue_key.append(self.driver.find_element(*self.ticket_id).get_attribute('data-issue-key')[-5:])
            return True
        return False

    def search_for_ticket(self, ticket):
        Waits.waitForElementIsVisible(self.driver, self.search). \
            send_keys(self.issue_key[0] + Keys.ENTER) if (ticket == 'my_ticket') else \
            Waits.waitForElementIsVisible(self.driver, self.search). \
                send_keys('abc' + str(randint(0, 100) * 12) + Keys.ENTER)
        return Waits.elementIsPresent(self.driver, self.search_validation_point)

    def search_for_few_ticket(self):
        Waits.waitForElementIsVisible(self.driver, self.issues_button).click()
        Waits.waitForElementIsClickable(self.driver, self.reported_by_me_button).click()
        return len(Waits.waitForElementsArePresent(self.driver, self.my_issue))

    def update_ticket(self, goal):
        self.search_for_ticket('my_ticket')
        result = False
        Waits.waitForElementIsClickable(self.driver, self.edit_issue_button).click()
        if goal == 'summary':
            result = self.__change_summary()
        elif goal == 'priority':
            result = self.__change_priority()
        elif goal == 'assignee':
            result = self.__change_assignee()
        return result

    def delete_ticket(self):
        self.search_for_ticket('my_ticket')
        Waits.waitForElementIsVisible(self.driver, self.more_button).click()
        Waits.waitForElementIsClickable(self.driver, self.delete_issue).click()
        Waits.waitForElementIsVisible(self.driver, self.delete_issue_submit).click()
        return Waits.elementIsPresent(self.driver, self.ticket_is_deleted)

    def __change_summary(self):
        Waits.waitForElementIsVisible(self.driver, self.input_summary).send_keys(self.updated_summary)
        Waits.waitForElementIsClickable(self.driver, self.update_issue_button).click()
        return Waits.elementIsPresent(self.driver, self.summary_value)

    def __change_priority(self):
        Waits.waitForElementIsClickable(self.driver, self.priority_field).send_keys('Low' + Keys.ENTER)
        Waits.waitForElementIsVisible(self.driver, self.update_issue_button).click()
        return Waits.elementIsPresent(self.driver, self.blocker)

    def __change_assignee(self):
        Waits.waitForElementIsVisible(self.driver, self.assign_to_me).click()
        Waits.waitForElementIsClickable(self.driver, self.update_issue_button).click()
        return Waits.elementIsPresent(self.driver, self.ticket_is_updated)

