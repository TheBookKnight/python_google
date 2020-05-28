from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# webdriver manager installs
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.google.com/")

driver.find_element_by_name("q").send_keys("Google")

driver.find_element_by_name("btnK").click()

time.sleep(2)

driver.close()
driver.quit()

print("Test Completed")