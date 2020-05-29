from Utils.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class SignInPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)  # explicit wait for 30s
        self.email_input = Locators.email_input_class
        self.next = Locators.next_btn_id
        self.sign_in_error = Locators.sign_in_error_class
        self.forgot_email = Locators.forgot_email_xpath
        self.forgot_email_directions = Locators.forgot_email_directions_xpath

    def go_to_sign_in_page(self):
        self.driver.get("https://accounts.google.com/")

    def enter_email_query(self, email):
        self.driver.find_element_by_class(self.email_input).clear()
        self.driver.find_element_by_class(self.email_input).send_keys(email)

    def click_forgot_email(self):
        self.driver.find_element_by_xpath(self.forgot_email).click()

    def click_next(self):
        self.driver.find_element_by_id(self.next).click()

    def return_error_message(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.sign_in_error)))
        return self.driver.find_element_by_class_name(self.sign_in_error).text

    def return_forgot_email_directions(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.forgot_email_directions)))
        return self.driver.find_element_by_xpath(self.forgot_email_directions).text