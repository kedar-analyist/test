import os
import time
from selenium import webdriver

chromedriver = "C:/SELENIUM DRIVERS/CD/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.google.com/")
print("Testcase Success")
