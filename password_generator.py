import random

# Generate a random number between 0 and 100
random_number = random.randint(0, 100)
print(random_number)

# Generate a random character from a-z
random_char = random.choice('abcdefghijklmnopqrstuvwxyz')
print(random_char)

# Generate a list of 5 unique random numbers between 0 and 100
random_numbers = random.sample(range(0, 101), 5)
print(random_numbers)

# Generate a list of 5 random characters from a-z
random_chars = random.choices('abcdefghijklmnopqrstuvwxyz', k=5)
print(random_chars)
