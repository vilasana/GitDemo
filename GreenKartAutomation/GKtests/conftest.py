from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import openpyxl
import logging
global driver

@pytest.fixture(scope="class")
def getBrowser(request):
    #if browser=="Chrome":

    #if browser=="Firefox":
        #driver = webdriver.Firefox()
    #elif browser=="IE":
    #    driver = webdriver.Ie()
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    request.cls.driver = driver

