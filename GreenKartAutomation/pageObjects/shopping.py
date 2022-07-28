from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utilities.BaseClass import baseClass

class shopping:
    def __init__(self,driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='products']/div/div/button")
    def getItems(self):
        return self.driver.find_elements(*shopping.products)

    def waitforitems(self):
        wait = WebDriverWait(self.driver, 4)
        wait.until(EC.element_to_be_clickable(shopping.products))

    def scrolltoTop(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")

    checkoutbtn = (By.CSS_SELECTOR, "img[alt*='Cart']")
    def checkitems(self):
        return self.driver.find_element(*shopping.checkoutbtn)

    selecteditems = (By.CSS_SELECTOR, "div[class*='cart-preview active'] div ul li")
    def itemschosen(self):
        return self.driver.find_elements(*shopping.selecteditems)

    removeItems = (By.XPATH, "//div[@class='cart-preview active']/div/div/ul/li")
    def getcostlyitems(self):
        return self.driver.find_elements(*shopping.removeItems)

    def proceedCheckout(self):
        self.driver.find_element(By.XPATH, "//div[@class='action-block']/button").click()















