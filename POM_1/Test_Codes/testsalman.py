from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Test_Locators import locators
from Test_Data import data
import pytest


class Test_Salman:
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()
   
   
    # Test Login
    def test_Login(self, booting_function):
       self.driver.get(data.Salman_Data().url)
       sleep(5)
       self.driver.find_element(by=By.NAME, value=locators.Salman_Locators().username_inputBox).send_keys(data.Salman_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Salman_Locators.password_InputBox).send_keys(data.Salman_Data.password)
       self.driver.find_element(by=By.XPATH, value=locators.Salman_Locators.LoginButton).click()
       assert self.driver.title == 'OrangeHRM'
       print("The User is Logged in Successfuly")

