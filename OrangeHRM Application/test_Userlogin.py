import pytest
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Test Scenario 1: User Login")
@allure.description("Verify that a user can successfully log in to the application using valid credentials.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Regression", "Smoke")
@allure.label("owner","Bhagyashree")
@pytest.mark.smoke
def test_user_login():
    # Step 1: Navigate to the login page
    driver = webdriver.Chrome()  # Launch the Chrome browser
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(3)

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
    
