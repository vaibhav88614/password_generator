import secrets
import nltk
import string

# Function to replace specific characters in words with special characters
def replace_special_characters(word):
    # Define replacements for specific characters
    replacements = {
        'a': '@',
        'A': '@',
        's': '$',
        'S': '$',
        'i': '!',
        'I': '!',
        'o': '*',
        'O': '*',
        't': '+',
        'T': '+'
        # Add more replacements as needed
    }
    
    # Check if the word already has two special characters
    special_count = sum(1 for char in word if char in string.punctuation)
    if special_count >= 2:
        return word  # Return the original word if it already has two special characters

    # Replace characters in the word if found in replacements
    new_word = ''.join(replacements.get(char, char) for char in word)
    return new_word

# Function to generate passphrase with option to include special characters
def generate_passphrase(num_words, include_special_chars=False):
    nltk.download('words')
    from nltk.corpus import words as nltk_words
    word_list = nltk_words.words()

    if include_special_chars:
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    else:
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    secure_random = secrets.SystemRandom()
    passphrase = []

    # Generate words and replace special characters as needed
    for _ in range(num_words):
        word = secure_random.choice(word_list)
        if include_special_chars:
            word = replace_special_characters(word)
        passphrase.append(word)

    # Add special characters if requested
    if include_special_chars:
        for _ in range(3):  # Ensure at least 3 special characters
            special_char = secure_random.choice(string.punctuation)
            passphrase.append(special_char)

    # Shuffle the passphrase for randomness
    secure_random.shuffle(passphrase)
    
    # Join passphrase into a single string
    passphrase = ' '.join(passphrase)
    
    return passphrase

def main():
    min_words = 4
    max_words = 6

    try:
        num_words = int(input(f"Enter number of words in passphrase ({min_words}-{max_words} words): "))
        if num_words < min_words or num_words > max_words:
            raise ValueError(f"Number of words must be between {min_words} and {max_words}.")

        include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

        passphrase = generate_passphrase(num_words, include_special_chars)
        print(f"Generated passphrase: {passphrase}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
