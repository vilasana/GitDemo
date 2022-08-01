from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pageObjects.placeorder import placeorder
from utilities.BaseClass import baseClass

class shopping:
    def __init__(self,driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='products']/div/div/button")
    def getItems(self):
        return self.driver.find_elements(*shopping.products)

    def waitforitems(self):
        wait = WebDriverWait(self.driver,5)
        wait.until(EC.element_to_be_clickable(shopping.products))

    checkoutbtn = (By.CSS_SELECTOR, "img[alt*='Cart']")
    def checkitems(self):
        self.driver.find_element(*shopping.checkoutbtn).click()

    selecteditems = (By.CSS_SELECTOR, "div[class*='cart-preview active'] div ul li")
    def seeitemschosen(self):
        si = self.driver.find_elements(*shopping.selecteditems)
        for item in si:
            self.driver.execute_script("arguments[0].scrollIntoView();", item)
            time.sleep(0.1)

    removeItems = (By.XPATH, "//div[@class='cart-preview active']/div/div/ul/li")
    def removecostlyitems(self):
        costlyitems = self.driver.find_elements(*shopping.removeItems)
        print("Following items removed due to high price:")
        for removeItem in costlyitems:
            remove = removeItem.find_element(By.XPATH, "div/p[2]")
            if int(remove.text) > 500:
                print(removeItem.find_element(By.XPATH,"div/p[1]").text)
                removeItem.find_element(By.XPATH,"a").click()

    btn = (By.XPATH, "//div[@class='action-block']/button")
    def proceedCheckout(self):
        self.driver.find_element(*shopping.btn).click()
        orderobj = placeorder(self.driver)
        return orderobj
















