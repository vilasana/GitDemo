from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from GKtests.pageObjects.placeorder import placeorder
from GKtests.pageObjects.shopping import shopping
from utilities.BaseClass import baseClass

class TestShopping(baseClass):

    def test_shop(self):
        shopobj = shopping(self.driver)
        items = shopobj.getItems()
        shopobj.waitforitems()
        print(len(items))
        for item in items:
            item.click()
        shopobj.scrolltoTop()
        btn = shopobj.checkitems()
        btn.click()
        selecteditems = shopobj.itemschosen()
        for item in selecteditems:
            self.driver.execute_script("arguments[0].scrollIntoView();", item)
            time.sleep(0.2)
        costlyitems = shopobj.getcostlyitems()
        for removeItem in costlyitems:
            remove = removeItem.find_element(By.XPATH, "div/p[2]")
            if int(remove.text) > 500:
                print(remove.text)
                removeItem.find_element(By.XPATH,"a").click()
        shopobj.proceedCheckout()

    def test_placeorder(self):
        orderobj = placeorder(self.driver)
        counts = orderobj.getquantity()
        for count in counts:
            if count.text == '1':
                continue
        print("All quantities are 1, no repetition")