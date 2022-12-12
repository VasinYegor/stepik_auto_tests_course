from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    browser.execute_script("window.scrollBy(0, 100);")
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsrule")
    option2.click()
    option3 = browser.find_element(By.CSS_SELECTOR, ".btn")
    option3.click()
finally:
    time.sleep(10)
    browser.quit()