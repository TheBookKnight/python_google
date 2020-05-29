from Utils.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)  # explicit wait for 30s

        self.search_textbox = Locators.search_textbox_name
        self.search_icon = Locators.search_icon_class
        self.search_result_stats = Locators.search_results_stats_id

    def go_to_results_page_for_query(self, query):
        self.driver.get("http://google.com/search?q="+query)
        self.wait_for_results()

    def wait_for_results(self):
        self.wait.until(EC.presence_of_element_located((By.ID, self.search_result_stats)))

    def enter_search_query(self, query):
        self.driver.find_element_by_name(self.search_textbox).clear()
        self.driver.find_element_by_name(self.search_textbox).send_keys(query)

    def click_search(self):
        self.driver.find_element_by_class(self.search_icon).click()

    def get_stats_from_results(self):
        self.wait_for_results()
        return self.driver.find_element_by_id(self.search_result_stats).text