import allure
import pytest
from selenium import webdriver


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
