from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login():
    driver = webdriver.Chrome()
    driver.get("https://demo.opencart.com/index.php?route=account/login")  # Direct login page

    # ✅ Enter Credentials (Invalid Example)
    username = "nanurag965@gmail.com"  # ❌ Wrong email
    password = "anurag123"  # ❌ Wrong password

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='input-email']"))
    ).send_keys(username)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='input-password']"))
    ).send_keys(password)

    # ✅ Click Login Button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
    ).click()

    time.sleep(2)  # Wait a bit for the popup to appear

    # ✅ Handle Successful Login
    try:
        success_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='My Account']"))
        )
        if success_message.text == "My Account":
            print("✅ Login successful")
            return driver  # ✅ Keep browser open for further tests

    # ❌ Handle Login Failure (Toast Notification)
    except:
        try:
            error_popup = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//dirv[@class='alert alert-danger alert-dismissible']"))
            )
            print(f"❌ Login failed: {error_popup.text}")
        except:
            print("❌ Login failed - Toast notification disappeared too fast!")





# If screenshot is required, then use this function
# def login():
#     driver = webdriver.Chrome()
#     driver.get("https://demo.opencart.com/index.php?route=account/login")  # Direct login page
#     driver.maximize_window()

#     # ✅ Enter Credentials (Invalid Example)
#     username = "wrongemail@gmail.com"  # ❌ Wrong email
#     password = "wrongpassword"  # ❌ Wrong password

#     WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@id='input-email']"))
#     ).send_keys(username)

#     WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.XPATH, "//input[@id='input-password']"))
#     ).send_keys(password)

#     # ✅ Click Login Button
#     WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
#     ).click()

#     time.sleep(2)  # Wait a bit for the popup to appear

#     # ✅ Handle Successful Login
#     try:
#         success_message = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='My Account']"))
#         )
#         if success_message.text == "My Account":
#             print("✅ Login successful")
#             return driver  # ✅ Keep browser open for further tests

#     # ❌ Handle Login Failure (Toast Notification)
#     except:
#         try:
#             error_popup = WebDriverWait(driver, 2).until(
#                 EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert-danger')]"))
#             )
#             print(f"❌ Login failed: {error_popup.text}")
#         except:
#             print("❌ Login failed - Toast notification disappeared too fast!")

#         driver.quit()  # Close browser if login fails

# # ✅ Run the function
# driver = login()
