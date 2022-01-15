import pytest
from selenium import webdriver
from pathlib import *
from chromedriver_py import binary_path


class TestLogin:
    @pytest.fixture()
    def test_setup(self):
        try:
            global driver
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')

            driver = webdriver.Chrome(executable_path=binary_path, chrome_options=chrome_options)
            driver.implicitly_wait(10)
            driver.maximize_window()
            yield
            driver.close()
            driver.quit()
            print("Test Completed")
        except:
            print("Something is failing")

    def test_01_login(self, test_setup):
        try:
            driver.get("http://20.204.191.213:5000/")
            print("Testing is Success")
        except:
            print("Something is failing")
            assert False

    '''
    def test_teardown():
        driver.close()
        driver.quit()
        print("Test Completed")
    '''
