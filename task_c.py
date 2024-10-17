# Function to check if the password is valid
def is_valid_password(password):
    # Check if the password contains at least one digit and one letter
    has_digit = any(char.isdigit() for char in password)  # Checks if the password has a number
    has_letter = any(char.isalpha() for char in password)  # Checks if the password has a letter
    # The password must be at least 8 characters long and contain both letters and numbers
    if len(password) >= 8 and has_digit and has_letter:
        return True  # Password is valid
    else:
        return False  # Password is invalid

# Ask the user to enter a password
password = input("Enter a password: ")

# Validate the password
if is_valid_password(password):
    print("Your password is valid")  # If the password meets the requirements
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")
    # If the password doesn't meet the requirements
    
 