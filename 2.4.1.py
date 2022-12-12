from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100")
        )

    button = browser.find_element(By.ID, "book")
    button.click()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)
finally:
    time.sleep(15)
    browser.quit()
