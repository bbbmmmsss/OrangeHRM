# API Testing
# ○ Description: Test the API endpoint that provides product details.
# ○ Steps:
# 1. Send a GET request to the
# https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/ad
# min/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC
# endpoint.
# 2. Verify that the response status code is 200.
# 3. Validate the structure of the response JSON, ensuring it contains user
# details like username, role, status, etc.
# 4. Verify the correctness of the data against the UI.

import requests
import jsonschema
from jsonschema import validate

# Step: 1. Send a GET request to the
# # https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/ad
# # min/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC endpoint.

response = requests.get("https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC")
print(response.status_code)
print(response.json())
print(response.headers)
print(response.cookies)
try:
    response.raise_for_status()
    print("Response JSON is valid")
    print(response.json())
    print(response.json()["users"][0]["userName"])
    print(response.json()["users"][0]["userRole"])
    print(response.json()["users"][0]["status"])

# 2. Verify that the response status code is 200.
except ValueError as ve:
    print("Response JSON is invalid:", ve)
    print("Test case failed - error")
    exit(1)
    print("Test case passed - 200 ok")
    exit(0)

# 3. Validate the structure of the response JSON, ensuring it contains user
# details like username, role, status, etc.
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

    user_schema = {
        "type": "object",
        "properties": {
            "users": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "role": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["username", "role", "status"]
                }
            }
        },
        "required": ["users"]
    }
    try:
        validate(instance=response.json(), schema=user_schema)
        print("Response JSON is valid")
        print("Test case passed")
        exit(0)
        print("Test case failed")
        exit(1)

# 4. Verify the correctness of the data against the UI.
    except jsonschema.exceptions.ValidationError as ve:
        print("Response JSON is invalid:", ve)
        print("Test case failed")
        exit(1)
        print("Test case passed")
        exit(0)
