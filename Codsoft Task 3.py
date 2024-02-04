import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if length <= 0:
        print("Invalid length. Please enter a positive number.")
        return

    generated_password = generate_password(length)
    print(f"\nGenerated Password: {generated_password}")

# Run the password generator
password_generator()
