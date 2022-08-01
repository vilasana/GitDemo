from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pageObjects.placeorder import placeorder
from pageObjects.shopping import shopping
from utilities.BaseClass import baseClass

class TestShopping(baseClass):

    def test_shop(self):
        shopobj = shopping(self.driver)
        items = shopobj.getItems()
        shopobj.waitforitems()
        self.clickitem(items)
        self.scrolltoTop()
        shopobj.checkitems()
        shopobj.seeitemschosen()
        shopobj.removecostlyitems()

        orderob = shopobj.proceedCheckout()
        orderob.checkredundantitems()
        self.scrolltoBottom()
        orderob.getpromocode()
       # orderob.comparePrice()
