import random
import string

length = int(input("Enter password length: "))

print("Include digits? (yes/no)")
use_digits = input().lower() == "yes"

print("Include special characters? (yes/no)")
use_symbols = input().lower() == "yes"

chars = string.ascii_letters

if use_digits:
    chars += string.digits

if use_symbols:
    chars += string.punctuation

password = ""

for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)
