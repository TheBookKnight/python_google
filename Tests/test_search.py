from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from Pages.SearchPage import SearchPage
from Pages.ResultsPage import ResultsPage


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_defaultSearchButtonText(self):
        driver = self.driver
        search_page = SearchPage(driver)
        search_page.go_to_home_page()
        self.assertEqual("Google Search",
                         search_page.get_text_from_element_name(search_page.search_btn),
                         "Btn SHOULD be 'Google Search'")
        self.assertRegex(search_page.get_text_from_element_name(search_page.im_feeling_lucky_btn),
                         "(I'm Feeling)(.*)",
                         "Btn SHOULD be 'I'm Feeling ...'")

    def test_enterSearchQueryGoesToResults(self):
        driver = self.driver
        search_page = SearchPage(driver)
        search_page.go_to_home_page()
        search_page.enter_search_query("Google")
        search_page.click_search()
        results_page = ResultsPage(driver)
        results_page.wait_for_results()
        self.assertRegex(results_page.get_stats_from_results(),
                         "(.*)(results \\()(.*)(seconds)(\\))",
                         "Given search query, when you click search button, then it SHOULD display result stats ")

    def test_signInDisplaysByDefault(self):
        driver = self.driver
        search_page = SearchPage(driver)
        search_page.go_to_home_page()
        self.assertEqual(driver.find_element_by_id(search_page.sign_in_btn).text,
                         "Sign in",
                         "By default, when on Search page without sign in token, then you SHOULD see the Sign In Page")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Search Tests Completed")


if __name__ == '__main__':
    unittest.main()