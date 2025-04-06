Make Your Test Reusable and Maintainable
Use variables for selectors or consider using a Page Object Model for bigger tests.

Add Logging or Print for Debugging
During development, it might help to log the actual values:

print(f"Text: {success_message_text}")
print(f"Color: {success_message_color}")

Parametrize Your Test (if using pytest)
You could test multiple usernames/passwords by parameterizing the function:

import pytest

@pytest.mark.parametrize("user_name,user_password", [
    ("user", "pwd"),
    ("admin", "admin123"),
])
def test_success_login_message(user_name, user_password):
    # Same test body here
