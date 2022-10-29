from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\Akash\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://www.youtube.com/")
print(driver.title)
print(driver.current_url)

driver.get("https://www.google.com/")
driver.minimize_window()

driver.close()