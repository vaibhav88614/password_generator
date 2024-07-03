import secrets
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    secure_random = secrets.SystemRandom()
    password = ''.join(secure_random.choice(alphabet) for _ in range(length))
    return password

def main():
    min_length = 10
    max_length = 64

    try:
        length = int(input(f"Enter password length ({min_length}-{max_length} characters): "))
        if length < min_length or length > max_length:
            raise ValueError(f"Password length must be between {min_length} and {max_length} characters.")
        
        password = generate_password(length)
        print(f"Generated password: {password}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
