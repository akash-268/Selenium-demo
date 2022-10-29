from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\Akash\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID, "checkBoxOption1").click()

# Dropdown
li = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for i in li:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()
        break

# Radio button
li2 = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
for i in li2:
    if i.get_attribute("value") == "radio3":
        i.click()
        assert i.is_selected()
        break

print(driver.find_element(By.ID, "displayed-text").is_displayed())
driver.find_element(By.ID, "hide-textbox").click()
print(driver.find_element(By.ID, "displayed-text").is_displayed())

# handling alert popups
name = 'Akash'
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
msg = alert.text
print(msg)
alert.accept()
assert name in msg
