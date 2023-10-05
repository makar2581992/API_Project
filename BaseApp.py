import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://test-stand.gb.ru'

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"can't fint element by locator {locator}")
        except:
            logging.exception("find element exception")
            element = None

        return element

    def get_element_property(self, locator, property_elem):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property_elem)
        else:
            logging.error(f'Property {property_elem} not found in element with locator {locator}')
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open site')
            start_browsing = None

        return start_browsing

    def get_alert(self):
        try:
            alert = self.driver.switch_to.alert
            return alert
        except:
            logging.exception('Exception with alert')
            return None