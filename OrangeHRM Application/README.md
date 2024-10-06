## A) First Step
-I have done code in Python with selenium by using **pytest framework**
-next step is  install all the required framework for the project

## B) Second Step
## First Scenario# 1 :User Login
    - ### Test Scenario 1: User Login
- we have Valid username and password credentials are available for testing.
- The presence of a specific user element indicates successful login.

**Steps:**
1. **Navigate to the login page.**
   - URL: [https://opensource-demo.orangehrmlive.com]
2. Assumption:
   - url is valid nedd t go login page
  
3. **Enter a valid username and password.**
   - Input: 
     - Username: Admin
     - Password: admin123

4. **Click on the "Login" button.**

**Verify successful login.**
   - Check for the presence of a user-specific element (e.g., a profile picture or username display).
   - Expected outcome: User-specific element is visible, confirming successful login.

**Post-conditions:**
- User should be redirected to the dashboard or home page upon successful login.

## First Scenario# 2 :User Management Search
- We have automate the search functionality for user management.

1. **Assumptions:**

The user is already logged in and has appropriate permissions to access the user management section.
The search bar is functional and located on the user management page.
There are existing users in the system that match the search keyword.

2. **Steps:**

Ensure the user is logged in.

Confirm that the user is on the user management page.
Search for a user ("Bhuvaneshwar") using the search bar.

Input: Enter "Bhuvaneshwar" in the search field and initiate the search.
Verify that search results are displayed and contain the search keyword.

**Expected outcome:** At least one search result should appear with the name "Bhuvaneshwar" or relevant matches.
Validate that the user details page can be opened from the search results.

Click on the user’s name in the search results.
Expected outcome: The user details page for "Bhuvaneshwar" is displayed correctly.

**Post-conditions:**
The user should be able to view and interact with the details of the searched user.

## First Scenario# 3 :Add New User


**Description:** Automate the process of adding a new user in the application.

1. **Assumptions:**
- The user is logged in with sufficient permissions to add new users.
- The user management page is accessible and functional.
- Valid values for `Bhuvaneshwar` and `Bhagu` placeholders will be provided during the test.

**Steps:**
1. **Search for a user and navigate to its details page.**
   - Input: Enter a  or relevant identifier in the search bar to locate the existing user.
  
2. **Add the user:**
   - **User Role:** Select "Admin" from the dropdown.
   - **Employee Name:** Enter `Bhuvaneshwar`.
   - **Status:** Set to "Enable."
   - **Username:** Enter `Bhagu`.
   - **Password and Confirm Password:** Enter "Qwerty@123" in both fields.

3. **Submit the form to add the user.**

4. **Verify that the user is added successfully.**
   - Check for a confirmation message or success indicator.
   - Validate that the new user appears in the user list.

**Post-conditions:**
- The newly added user should be accessible in the user management system and have the specified roles and credentials.

## C) Third Step
## For Generate Allure Report
1. First i need to install "**pip install allure_pytest**"
2. For Run the allure command "**pytest OrangeHRM/test_Addnewuser.py --alluredir=allure_result** "
3. Install allure commandline for generate the link of allure report "**npm install -g allure-commandline**"
4. This is generate link of allure report **allure serve allure_result**