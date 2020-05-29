from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from Pages.SearchPage import SearchPage
from Pages.ResultsPage import ResultsPage


class ResultsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_enterSearchQueryStaysInResults(self):
        driver = self.driver
        results_page = ResultsPage(driver)
        results_page.go_to_results_page_for_query("Google")
        results_page.enter_search_query("Bing")
        results_page.wait_for_results()
        self.assertRegex(results_page.get_stats_from_results(),
                         "(.*)(results \\()(.*)(seconds)(\\))",
                         "Given search query, when you click search icon, then it SHOULD remain on result stats ")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
