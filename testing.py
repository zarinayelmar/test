from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")
driver.implicitly_wait(10)


locator3 = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button').click()
driver.implicitly_wait(10)
locator3 = driver.find_element(By.CSS_SELECTOR, '#input-example > button').click()
driver.implicitly_wait(10)
