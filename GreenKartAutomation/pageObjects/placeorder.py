from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import openpyxl
import logging

class placeorder:
    def __init__(self,driver):
        self.driver = driver

    quantity = (By.XPATH, "//table[@class='cartTable']/tbody/tr/td[3]/p")
    def getquantity(self):
        return self.driver.find_elements(*placeorder.quantity)











