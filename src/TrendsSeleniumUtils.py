from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

def search(driver, keyword):
    input = driver.find_element(By.ID, "i7")
    input.clear()
    input.send_keys(keyword)
    time.sleep(1)
    input.send_keys(Keys.RETURN)
    time.sleep(7)

def selectDate(driver):
    datePicker = driver.find_element(By.TAG_NAME, "custom-date-picker")
    datePicker.click()
    time.sleep(0.2)
    date = driver.find_element(By.ID, "select_option_21")
    date.click()
    time.sleep(7)

def downloadFile(driver):
    downloadButtons = driver.find_elements(By.XPATH, "//button[@class='widget-actions-item export']")
    for button in downloadButtons:
        try:
            button.click()
            time.sleep(3)
            return
        except:
            pass

