### **Problem: Email Address Validator**

#### **Background**
In software development, validating user input, such as email addresses, is a common task. A valid email address typically follows this format:

```
local_part@domain
```

- **local_part** is the part of the email address that identifies the user.
- **domain** is the part that specifies the email server's address.

#### **Task**
Design a function called `is_valid_email(email: str) -> bool` that validates a given email address based on the following rules.

---

#### **Validation Rules**

1. **Must contain `@` and `.`**
   - A valid email address must contain both `@` and `.`.
   - Example: `example@domain.com` is valid, but `exampledomain.com` is invalid.

2. **Correct splitting structure**
   - The email should be split into two parts:
     - **local_part**: before the `@`.
     - **domain**: after the `@`.
   - The `@` must be present in the middle, and both parts must be non-empty.
   - Example: `@domain.com` and `example@` are invalid.

3. **Domain rules**
   - The top-level domain (the last part of the domain) must have at least two characters.
   - Example: `example@domain.c` is invalid, but `example@domain.co` is valid.

4. **No consecutive dots**
   - The email must not contain consecutive dots (`..`).
   - Example: `example@domain..com` is invalid.

5. **No special characters at the start or end**
   - Neither the local part nor the domain should start or end with special characters like `.`, `-`, or `_`.
   - Example: `-example@domain.com` and `example@domain-.com` are invalid.

---

#### **Function Signature**
```python
def is_valid_email(email: str) -> bool:
    """
    Validates an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
```

---

#### **Test Cases**
After completing the function, validate it using the following test cases:

```python
# Test data
test_emails = [
    "test@example.com",        # Valid
    "user.name+tag@gmail.com", # Valid
    "user@sub.domain.com",     # Valid
    "invalid_email@",          # Invalid
    "@example.com",            # Invalid
    "plainaddress",            # Invalid
    "user@.com",               # Invalid
    "user@domain..com",        # Invalid
    "-user@domain.com",        # Invalid
    "user@domain.-com",        # Invalid
]

# Test function
for email in test_emails:
    print(f"{email}: {is_valid_email(email)}")
```

#### **Expected Output**
```
test@example.com: True
user.name+tag@gmail.com: True
user@sub.domain.com: True
invalid_email@: False
@example.com: False
plainaddress: False
user@.com: False
user@domain..com: False
-user@domain.com: False
user@domain.-com: False
```

---

#### **Requirements**
1. **Do not use `re` or any regular expression libraries.**
2. **Only use basic string operations such as `split`, `find`, etc.**
3. **Include comments in your implementation to explain your logic.**
