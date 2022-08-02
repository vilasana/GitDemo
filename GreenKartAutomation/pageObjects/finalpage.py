from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pytest
import openpyxl
import logging

class finalpage:

    def __init__(self,driver):
        self.driver = driver

    checkbox = (By.XPATH,"//input[@type='checkbox']")
    btn = (By.XPATH,"//button[text()='Proceed']")
    def choosecountry(self):
        #dd = Select()
        dd = Select(self.driver.find_element(By.TAG_NAME,"select"))
        dd.select_by_visible_text("India")
        self.driver.find_element(*finalpage.checkbox).click()
        self.driver.find_element(*finalpage.btn).click()
        sp = self.driver.find_element(By.XPATH,"//div[@class='wrapperTwo']/span")
        #self.driver.execute_script("window.stop();")
        if "placed" in sp.text:
            print("Order placed successfully")
        else:
            print("Sorry")




