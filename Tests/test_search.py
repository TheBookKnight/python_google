from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Google")
        self.driver.find_element_by_name("btnK").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

# allows you to run python tests by "python <file_name>"
if __name__ == '__main__':
    unittest.main()