from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from login import login  # Assuming login function is in login.py
from cart_page import add_to_cart


def checkout(driver):
    if driver is None:
        print("No driver")
        return
    try:
        checkout_button = driver.find_element(By.XPATH, "//button[text()='Checkout']")

        checkout_button =  WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn btn-primary"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", checkout_button)
        checkout_button.click()


    except Exception as e:
        print(f"Add product to cart {e}")

    # Opens login page and logs in


driver = login()

# Opens cart page in same browser
if driver:
    add_to_cart(driver)

# opens cart page in same browser
if driver:
    checkout(driver)

if driver:
    print("completed checkout")
