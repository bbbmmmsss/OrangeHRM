import pytest
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@allure.title("Test Scenario 3: Add to new user")
@pytest.mark.smoke
def test_add_new_user():
    # Step 1: Navigate to the login page
    driver = webdriver.Chrome()  # Launch the Chrome browser
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(3)
    driver.maximize_window()

    # Step 2: Enter valid username and password
    driver.find_element(By.CSS_SELECTOR,"div.oxd-form-row:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin123")
    time.sleep(5)

    # Step 3: Click on the login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # Step 4: Verify successful login by checking the presence of a user-specific element.
    driver.find_element(By.XPATH,"//span[@class='oxd-topbar-header-breadcrumb']//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    assert 'Dashboard' == "Dashboard"

    time.sleep(2)


    # Step 1: Navigate to the user management page
    driver.find_element(By.XPATH, "//span[text()='Admin']").click()
    time.sleep(5)

    # Wait for the page to load and go to "User Management > Users"
    driver.find_element(By.XPATH, "//span[contains(text(),'User Management')]").click()
    time.sleep(5)

    # Step 2: Enter the username to search
    driver.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@class='oxd-input oxd-input--active']").send_keys("Bhuvaneshwar")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    # Take screenshot
    driver.save_screenshot("C:\OrangHRM Screenshot\Screenshot1.png")

    time.sleep(2)


    # step 3: Add new User
    driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
    time.sleep(5)

    # Select User Role
    driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input'][1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@role='listbox']//div[2]").click()
    time.sleep(2)

    # Enter Employee Name= Mahmoud W Aboelnasr
    driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("Lucy Limchiya Williams")
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@role='listbox']//div[1]").click()
    time.sleep(2)

    # Select Status
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(1) > div > div:nth-child(3) > div > div:nth-child(2) > div")


    # Enter Username
    #driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("Bhagu")
    driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(1) > div > div:nth-child(4) > div > div:nth-child(2) > input").send_keys("Bhagu")
    time.sleep(2)

    # Enter Password
    driver.find_element(By.XPATH,"(//input[@type='password'])[1]").send_keys("Qwerty@123")
    time.sleep(2)

    # Confirm Password
    driver.find_element(By.XPATH,"(//input[@type='password'])[2]").send_keys("Qwerty@123")
    time.sleep(2)

    # Save the new User
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # Verify the User Creation
    assert 'Successfully Saved' == "Successfully Saved"

    time.sleep(5)

    # Close the browser
    driver.quit()





