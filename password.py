#task 2
import random
import string

print("Random Password Generator")

# Ask user for password length
length = int(input("Enter desired password length: "))

# Ask user for character types
include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include special characters? (y/n): ").lower() == 'y'

# Build character pool based on user choices
characters = ""
if include_upper:
    characters += string.ascii_uppercase
if include_lower:
    characters += string.ascii_lowercase
if include_digits:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

# Ensure user selected at least one option
if not characters:
    print("Error: You must select at least one character type!")
else:
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    print("\n Generated Password:", password)
