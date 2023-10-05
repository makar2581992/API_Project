import time
import logging
import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TestSearchLocators:
    ids = dict()
    with open('./locators.yaml', encoding='utf-8') as fy:
        locators = yaml.safe_load(fy)
        for locator in locators['xpath'].keys():
            ids[locator] = (By.XPATH, locators['xpath'][locator])
        for locator in locators['css'].keys():
            ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationHelper(BasePage):

    # ENTER
    def enter_text_into_field(self, locator, text, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'send work "{text}" in element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'element {locator} - not found')
            return False
        try:
            field.clear()
            field.send_keys(text)
        except:
            logging.exception(f'Exception while operation in locator {locator}')
            return False
        return True

    def enter_login(self, login):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], login, description='login form')

    def enter_pass(self, password):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], password, description='password form')

    def enter_title_new_post(self, title):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_TITLE_NEW_POST'], title,
                                   description='Title new post')

    def enter_description_new_post(self, description):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_DESC_NEW_POST'], description,
                                   description='description new post')

    def enter_content_new_post(self, content):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTENT_NEW_POST'], content,
                                   description='content new post')

    def enter_contact_us_name(self, name):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_US_NAME'], name,
                                   description='name form "Contact Us"')

    def enter_contact_us_email(self, email):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_US_EMAIL'], email,
                                   description='email form "Contact Us"')

    def enter_contact_us_content(self, content):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_US_CONTENT'], content,
                                   description='content form "Contact Us"')

    # CLICKER
    def click_botton(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        button = self.find_element(locator, time=10)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception(f'Exception with click')
            return False

        logging.debug(f'Clicked  {element_name} button')
        return True

    def click_login_botton(self):
        self.click_botton(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login')

    def click_new_post_botton(self):
        self.click_botton(TestSearchLocators.ids['LOCATOR_BTN_NEW_POST'], description="new post")

    def click_save_new_post(self):
        self.click_botton(TestSearchLocators.ids['LOCATOR_BTNSAVE_NEW_POST'], description="save post")

    def click_page_contact(self):
        self.click_botton(TestSearchLocators.ids['LOCATOR_CONTACT_US'], description="Contact")
        time.sleep(2)

    def click_button_contact_us(self):
        self.click_botton(TestSearchLocators.ids['LOCATOR_CONTACT_US_BUTTON'], description="Contact us")

    # GETTER
    def get_text_from_element(self, locator, description):
        if description:
            element_name = description
        else:
            element_name = locator

        field = self.find_element(locator, time=10)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.debug(f'We find {text} in field {element_name}')
        return text

    def get_title_save_post(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_TITLE_SAVE_POST'], description='title post')

    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='text errror')

    def get_success_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_SUCCESS'], description='text success')

    def get_success_page_contact_us(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_TEXT_CONTACT_US'], description='Contact US')

    def get_alert_text(self):
        text = self.get_alert().text
        logging.info(f"get alert text {text}")
        return text