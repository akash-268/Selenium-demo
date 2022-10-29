from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\Akash\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "name").send_keys("Akash Bajpai")
driver.find_element(By.NAME, "email").send_keys("akashbajpai@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("aka475pai")
driver.find_element(By.ID, "exampleCheck1").click()
s = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
s.select_by_index(1)

age = 25
if age < 18:
    driver.find_element(By.ID, "inlineRadio1").click()
else:
    driver.find_element(By.ID, "inlineRadio2").click()
