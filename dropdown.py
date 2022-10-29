import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Akash\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
li = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
for i in li:
    if i.text == "India":
        i.click()
        break

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
