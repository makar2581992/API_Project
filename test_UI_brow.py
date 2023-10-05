import pytest
import time

from testpage import OperationHelper
import yaml

with open('testdata.yaml') as fy:
    testdata = yaml.safe_load(fy)


def test_authorize_invalid(browser):
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_botton()

    assert testpage.get_error_text() == '401'


@pytest.mark.contact
def test_authorize_valid(browser):
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_botton()

    assert testpage.get_success_text() == f'Hello, {testdata["username"]}', 'not enty'


def test_add_new_post(browser):
    testpage = OperationHelper(browser)
    testpage.click_new_post_botton()
    testpage.enter_title_new_post(testdata['title'])
    testpage.enter_description_new_post(testdata['description'])
    testpage.enter_content_new_post(testdata['content'])
    testpage.click_save_new_post()

    assert testpage.get_title_save_post() == testdata['title']


@pytest.mark.contact
def test_contact_us_open(browser):
    testpage = OperationHelper(browser)
    testpage.click_page_contact()

    assert testpage.get_success_page_contact_us() == testdata['Contact_us']


@pytest.mark.contact
def test_contact_us_alert(browser):
    testpage = OperationHelper(browser)
    testpage.enter_contact_us_name(testdata['username'])
    testpage.enter_contact_us_email(testdata['email'])
    testpage.enter_contact_us_content(testdata['content_CU'])
    testpage.click_button_contact_us()
    time.sleep(3)
    text_alert = testpage.get_alert_text()
    assert text_alert == testdata['alert']