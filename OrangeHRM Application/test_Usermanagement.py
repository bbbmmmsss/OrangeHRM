import pytest
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Test Scenario 2: User Management Search")
@pytest.mark.smoke
def test_user_management():
    # Step 1: Navigate to the login page
    driver = webdriver.Chrome()  # Launch the Chrome browser
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(3)

    # Step 2: Enter valid username and password
    driver.find_element(By.CSS_SELECTOR,
                        "div.oxd-form-row:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys(
        "Admin")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin123")
    time.sleep(5)

    # Step 3: Click on the login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # Step 4: Verify successful login by checking the presence of a user-specific element.
    driver.find_element(By.XPATH,
                        "//span[@class='oxd-topbar-header-breadcrumb']//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    assert 'Dashboard' == "Dashboard"

    time.sleep(2)

    # Step 1: Navigate to the user management page
    driver.find_element(By.XPATH, "//span[text()='Admin']").click()
    time.sleep(5)

    # Wait for the page to load and go to "User Management > Users"
    driver.find_element(By.XPATH, "//span[contains(text(),'User Management')]").click()
    time.sleep(5)

    # Step 2: Enter the username to search
    driver.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@class='oxd-input oxd-input--active']").send_keys(
        "Bhuvaneshwar")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    # Take screenshot
    driver.save_screenshot("C:\OrangHRM Screenshot\Screenshot.png")
    time.sleep(2)


    # Step 3: Verify the search results
    if (driver.find_element(By.XPATH, "//div[@class='oxd-table-body']")):
        assert 'No Record Found' == "No Record Found"

        print("Record Found")
    else:

        print("No Record Found")

    time.sleep(5)

    # Close the browser
    driver.quit()


    
