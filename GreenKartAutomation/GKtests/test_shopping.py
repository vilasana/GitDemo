from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import openpyxl
import logging
from utilities.BaseClass import baseClass

class TestOne(baseClass):
    def test_addToCart(self):
        products = self.driver.find_elements(By.XPATH, "//div[@class='products']/div/div/button")
        print(len(products))
        for product in products:
            product.click()
        wait = WebDriverWait(self.driver,4)
        wait.until(EC.element_to_be_clickable(products[29]))
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")


    def test_CheckoutItems(self):
        checkoutbtn = self.driver.find_element(By.CSS_SELECTOR, "img[alt*='Cart']")
        checkoutbtn.click()
        items = self.driver.find_elements(By.CSS_SELECTOR, "div[class*='cart-preview active'] div ul li")
        for item in items:
            self.driver.execute_script("arguments[0].scrollIntoView();", item)
            time.sleep(0.2)

    def test_removeCostlyItems(self):
        removeItems = self.driver.find_elements(By.XPATH, "//div[@class='cart-preview active']/div/div/ul/li")
        for removeItem in removeItems:
            remove = removeItem.find_element(By.XPATH,"div/p[2]")
            if int(remove.text) > 500:
                print(remove.text)
                removeItem.find_element(By.XPATH,"a").click()
















