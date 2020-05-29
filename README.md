# My Python Selenium Demo on Google page 

Note: I used [PyCharm IDE](https://www.jetbrains.com/pycharm/) as it's easy to import necessary libraries and has an isolated virtual environment.

## Step 1: Ensure correct dependencies are installed

See the attached *requirements.txt*

Quickly check if you can navigate to Google by scripting some navigational code. See *test_search.py*

### NOTES
If you're facing ChromeDriver issues, use the [DriverManager library](https://stackoverflow.com/questions/60806988/selenium-error-this-version-of-chromedriver-only-supports-chrome-version-81-m) so it automatically installs the latest driver.

## Step 2: Test displaying Test Results
Setup your test script as a unit test file by the following:
1. Structure test as a class with param as "unittest.TestCase"
2. Create a setup and teardown method for your driver
    - annotate it with @classmethod 
3. Insert your webdriver script into the method
4. Go to "Run" > "Edit Configurations", then add your test file as a "Python Test"
    - make sure the target file is the class file you just created
5. When you right-click your python test file, you can click "Run" and it will run as unit tests
    - you can see results in your PyCharm IDE below

 
