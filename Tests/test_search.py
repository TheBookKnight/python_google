from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

from Pages.SearchPage import SearchPage


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        searchPage = SearchPage(driver)
        searchPage.go_to_home_page()
        searchPage.enter_search_query("Google")
        searchPage.click_search()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

# allows you to run python tests by "python <file_name>"
if __name__ == '__main__':
    unittest.main()