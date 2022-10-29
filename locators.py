from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Akash\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.LINK_TEXT, "Forgot password?").click() # text must be an anchor tag

driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("akash@redhat.com")
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("aka475pai")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("aka475pai")

p1 = driver.find_element(By.CSS_SELECTOR, "input[id='userPassword']").text
p2 = driver.find_element(By.CSS_SELECTOR, "input[id='confirmPassword']").text

if p1==p2:
    print("SUCCESS")
else:
    print("FAILURE")

driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()