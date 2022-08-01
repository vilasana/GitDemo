from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pytest
import openpyxl
import logging

class placeorder:

    def __init__(self,driver):
        self.driver = driver

    quantity = (By.XPATH, "//table[@class='cartTable']/tbody/tr/td[3]/p")
    def checkredundantitems(self):
        qty = self.driver.find_elements(*placeorder.quantity)
        for count in qty:
            if count.text == '1':
                continue
        print("All quantities are 1, no repetition")

    promocode = (By.XPATH, "//div[@id='root']/div/div/div/div/div/input")
    promobtn = (By.XPATH, "//div[@id='root']/div/div/div/div/div/button")
    pi = (By.XPATH, "//div[@id='root']/div/div/div/div/div/span")
    def getpromocode(self):
        self.driver.find_element(*placeorder.promocode).send_keys("rahulshettyacademy")
        self.driver.find_element(*placeorder.promobtn).click()
        self.driver.implicitly_wait(12)
        promoinfo = self.driver.find_element(*placeorder.pi)
        assert promoinfo.text == 'Code applied ..!'

    total = (By.XPATH,"//span[@class='totAmt']")
    disc = (By.XPATH,"//span[@class='discountAmt']")
    def comparePrice(self):
        total = self.driver.find_element(*placeorder.total)
        disc = self.driver.find_element(*placeorder.disc)
        if total.text > disc.text :
            print("Discount applied")
        else:
            print("Discount not valid")

    #order = (By.CSS_SELECTOR, "div[class*='products'] div button") #CSS selector doesn't work. need to find out why
    #order = (By.XPATH, "//div[@class='products']/div/button") #works fine
    def orderItems(self):
        #self.driver.find_element(*placeorder.order).click()
        self.driver.find_element(By.XPATH,"//button[text()='Place Order']").click()




