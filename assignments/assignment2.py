'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''
# Taking input from the user and sanitize it 
email = input("Enter an email address: ").strip()

# Check if the email address is valid
# is_valid = "." in email[-3:] and "@" in email[:-4] and " " not in email

# Results
# print(is_valid)

# testing
test_emails = ["test@mail.com","no@spaces.com","yes@mail.com"
               "farley@mail.com"]

# print("\nAdditional testing:")
# for test_email in test_emails:
#     is_valid = "." in test_email[-3:] and "@" in test_email[:-4] and " " not in test_email
#     print(f"{test_email}: {is_valid}")
# if len(email) >= 7 and "." in email[-2:] and "@" in email[:-3] and " " not in email:
#     print(True)
# else:
#     print(False)

# Check if the email address is valid
is_valid = len(email) >= 7 and "." in email[-3:] and "@" in email[:-4] and " " not in email

# Print the result
print(is_valid)

# Is the result now correct? (Yes/No)