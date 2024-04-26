#!/usr/bin/env python3
import random
import string

def generate_password(length=14):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage:
generated_password = generate_password()
print("Generated Password:", generated_password)
