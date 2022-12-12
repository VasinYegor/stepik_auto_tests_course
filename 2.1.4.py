from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    z = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x_element = z.get_attribute("valuex")
    x = x_element
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    option3 = browser.find_element(By.CSS_SELECTOR, ".btn")
    option3.click()
finally:
    time.sleep(5)
    browser.quit()