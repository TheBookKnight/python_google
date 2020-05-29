from Utils.Locators import Locators

class SearchPage():

    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_name = Locators.search_textbox_name
        self.search_btn_name = Locators.search_btn_name

    def go_to_home_page(self):
        self.driver.get("https://www.google.com/")

    def enter_search_query(self, query):
        self.driver.find_element_by_name(self.search_textbox_name).clear()
        self.driver.find_element_by_name(self.search_textbox_name).send_keys(query)

    def click_search(self):
        self.driver.find_element_by_name("btnK").click()