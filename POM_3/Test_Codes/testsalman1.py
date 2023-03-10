# app.py - The main executable file


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Test_Locators import Locators
from Test_Data import Data
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
       self.driver.get(Data.Salman_Data().url)
       sleep(5)
       self.driver.find_element(by=By.NAME, value=Locators.Salman_Locators.username_locator).send_keys(Data.Salman_Data.username)
       self.driver.find_element(by=By.NAME, value=Locators.Salman_Locators.password_locator).send_keys(Data.Salman_Data.password)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.loginButtonLocator).click()
       assert self.driver.title == 'OrangeHRM' 
       sleep(10)
       self.driver.get(Data.Salman_Data().url)
       sleep(10)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.PIM_Locator).click()
       sleep(5)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.employee_name).send_keys(Data.Salman_Data.employee_name)
       sleep(5)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.search).click()
       sleep(3)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.Aaliyah).click()
       sleep(3)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.lastname).send_keys(Data.Salman_Data.lastname)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.save).click()
       sleep(5)
       print("SUCCESSFUL EMPLOYEE ADDITION") 
       
       

       
       