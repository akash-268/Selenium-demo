from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Akash\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "name").send_keys("Akash Bajpai")
driver.find_element(By.NAME, "email").send_keys("akashbajpai@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("aka475pai")
