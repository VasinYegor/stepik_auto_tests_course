from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y = browser.find_element(By.CSS_SELECTOR, "#num2").text
    def sum(x, y):
        return str(int(x) + int(y))
    z = sum(x, y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)

    option3 = browser.find_element(By.CSS_SELECTOR, ".btn")
    option3.click()
finally:
    time.sleep(5)
    browser.quit()