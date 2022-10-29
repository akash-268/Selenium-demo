from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# -- Chrome
service_obj = Service(r"C:\Users\Akash\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# -- Firefox
# service_obj = Service(r"download and install gecko driver and give it's path")
# driver = webdriver.Firefox(service=service_obj)

# -- Microsoft Edge
# service_obj = Service(r"download and install microsoft edge driver and give it's path")
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()

driver.get("https://www.youtube.com/")
print(driver.title)
print(driver.current_url)

driver.get("https://www.google.com/")
#driver.minimize_window()

driver.back()
driver.refresh()
driver.forward()

driver.close()