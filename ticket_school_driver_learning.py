from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

LOGIN_CODE = "changxu878475nydd"
LOGIN_URL = "https://courses.ticketschool.com/nysdd/Account/Login"
# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# Navigate to a sample website (using Python.org as an example)
driver.get(LOGIN_URL)

# Wait for the login code input field to be present
code_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ViewModel_UserName"))  # Replace with actual locator
)

# Enter the login code (replace 'YOUR_CODE_HERE' with the actual code)
login_code = LOGIN_CODE
code_input.send_keys(login_code)

# Find and click the login button
login_button = driver.find_element("xpath", '//*[@id="main-container"]/div/div/div[1]/div/div/div/div/form/div[2]/div/button')  # Replace with actual locator
login_button.click()


while True:
    # Wait for the page with the countdown timer to load
    # Assuming the timer is displayed after login
    timer_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "page-timer"))  # Replace with actual locator
    )
    # Monitor the countdown timer
    while True:
        timer_text = timer_element.text.strip()  # Get the current timer value
        print(f"Current timer: {timer_text}")

        # Check if the timer reaches "00:00"
        if timer_text == "00:00":
            print("Timer reached 00:00!")
            time.sleep(1)
            break
        
        # Wait 1 second before checking again to avoid overwhelming the system
        time.sleep(1)
        # Refresh the timer element to get the latest value
        timer_element = driver.find_element(By.ID, "page-timer")  # Re-fetch to avoid stale element

    # Find and click the "Next" button when timer hits "00:00"
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main-container"]/div[2]/div/div/div[2]/div/div/div[2]/nav/ul/li[3]/a'))  # Replace with actual locator
    )
    next_button.click()
    print("Clicked the 'Next' button!")

    # Optional: Wait to see the result
    time.sleep(2)

