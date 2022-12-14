import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

actual = []
expected = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
service_obj = Service(r"C:\Users\Akash\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

query = 'ber'
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys(query)
time.sleep(1)
li = driver.find_elements(By.CSS_SELECTOR,
                          "div[class='products'] div[class='product'] div[class='product-action'] button")

li2 = driver.find_elements(By.CSS_SELECTOR,
                           "div[class='products'] div[class='product'] div[c"
                           "lass='product-action'] h4")

for i in li2:
    actual.append(i.text)
for i in li:
    i.click()
print(actual)
driver.find_element(By.CLASS_NAME, "cart-icon").click()
driver.find_element(By.CSS_SELECTOR, "div[class='action-block'] button").click()

sum = 0

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
for i in prices:
    sum += int(i.text)
print(sum)

x = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
assert x == sum

# driver.find_elements(By.CLASS_NAME,"amount").
driver.find_element(By.CSS_SELECTOR, "div[class='promoWrapper'] input[class='promoCode']").send_keys(
    "rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
assert driver.find_element(By.CLASS_NAME, "promoInfo").is_displayed()

y = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
assert y < x
