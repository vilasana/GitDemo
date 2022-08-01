from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_elements(By.XPATH,"//div[@class='product-action'][1]/button").click()
driver.find_element(By.XPATH,"//div[@class='cart-info']/a/img").click()
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("abc")