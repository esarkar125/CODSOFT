import random
import string

def generate_password(length, use_digits=True, use_special_chars=True):
    # Define character sets based on complexity requirements
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))

    if length <= 0:
        print("Password length should be greater than 0.")
    else:
        use_digits = input("Include digits (0-9)? (yes/no): ").lower().startswith('y')
        use_special_chars = input("Include special characters? (yes/no): ").lower().startswith('y')

        password = generate_password(length, use_digits, use_special_chars)

        print("Generated Password:", password)

if __name__ == "__main__":
    main()