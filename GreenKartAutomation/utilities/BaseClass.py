import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("getBrowser")
class baseClass():

    def scrolltoTop(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")

    def scrolltoBottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(0.5)

    def clickitem(self,items):
        for item in items:
            item.click()