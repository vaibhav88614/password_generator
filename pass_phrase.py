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

    # Initialize a counter for replaced specific characters
    replaced_count = 0

    # Iterate through each character in the word
    new_word = []
    for char in word:
        if char in replacements:
            if replaced_count < 2:  # Replace only if less than two characters replaced
                new_word.append(replacements[char])
                replaced_count += 1
            else:
                new_word.append(char)  # Keep the original character if already replaced twice
        else:
            new_word.append(char)  # Keep non-specific characters as-is

    # Join the list into a string
    modified_word = ''.join(new_word)

    return modified_word

# Function to generate passphrase with optional special characters
def generate_passphrase(num_words, include_special_chars=False):
    nltk.download('words')
    from nltk.corpus import words as nltk_words
    word_list = nltk_words.words()

    # Define the alphabet for special characters
    if include_special_chars:
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    else:
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits

    secure_random = secrets.SystemRandom()
    passphrase_words = []
    unfiltered_passphrase_words = []

    # Generate words and optionally replace special characters
    for _ in range(num_words):
        word = secure_random.choice(word_list)
        unfiltered_passphrase_words.append(word)  # Store original word

        # Replace special characters in the word if requested
        if include_special_chars:
            word = replace_special_characters(word)

        passphrase_words.append(word)

    # Join passphrases into a single string
    passphrase = ' '.join(passphrase_words)
    unfiltered_passphrase = ' '.join(unfiltered_passphrase_words)

    return passphrase, unfiltered_passphrase  # Return both filtered and unfiltered passphrases

def main():
    min_words = 4
    max_words = 6

    try:
        # Input number of words in passphrase
        num_words = int(input(f"Enter number of words in passphrase ({min_words}-{max_words} words): "))
        if num_words < min_words or num_words > max_words:
            raise ValueError(f"Number of words must be between {min_words} and {max_words}.")

        # Input whether to include special characters
        include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

        # Generate passphrase
        filtered_passphrase, unfiltered_passphrase = generate_passphrase(num_words, include_special_chars)

        # Print generated passphrases
        print(f"Generated passphrase (Filtered): {filtered_passphrase}")
        print(f"Generated passphrase (Unfiltered): {unfiltered_passphrase}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
