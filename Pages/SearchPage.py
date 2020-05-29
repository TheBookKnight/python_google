from Utils.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait


class SearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30) # explicit wait for 30s

        self.sign_in_btn = Locators.sign_in_btn_id
        self.search_textbox = Locators.search_textbox_name
        self.search_btn = Locators.search_btn_name
        self.im_feeling_lucky_btn = Locators.im_feeling_lucky_btn_name

    def go_to_home_page(self):
        self.driver.get("https://www.google.com/")

    def enter_search_query(self, query):
        self.driver.find_element_by_name(self.search_textbox).clear()
        self.driver.find_element_by_name(self.search_textbox).send_keys(query)

    def click_search(self):
        self.driver.find_element_by_name(self.search_btn).click()

    def get_text_from_element_name(self, name):
        value = self.driver.find_element_by_name(name).get_attribute('value')
        if value is None or value == "":
            value = self.driver.find_element_by_name(name).text
        return value
