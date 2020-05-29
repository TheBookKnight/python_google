from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest, time

from Pages.SignInPage import SignInPage


class SignInTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_enterNoEmail(self):
        driver = self.driver
        sign_in_page = SignInPage(driver)
        sign_in_page.go_to_sign_in_page()
        sign_in_page.click_next()
        self.assertEqual("Enter an email or phone number",
                         sign_in_page.return_error_message(),
                         "Given no email, when the user clicks next, then there SHOULD be an error message.")

    def test_forgotEmail(self):
        driver = self.driver
        sign_in_page = SignInPage(driver)
        sign_in_page.go_to_sign_in_page()
        sign_in_page.click_forgot_email()
        print(sign_in_page.return_forgot_email_directions())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Sign In Tests Completed")

if __name__ == '__main__':
    unittest.main()
