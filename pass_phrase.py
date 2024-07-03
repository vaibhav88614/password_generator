import secrets
import nltk

def generate_passphrase(num_words):
    nltk.download('words')
    from nltk.corpus import words as nltk_words
    word_list = nltk_words.words()

    secure_random = secrets.SystemRandom()
    passphrase = ' '.join(secure_random.choice(word_list) for _ in range(num_words))
    return passphrase

def main():
    min_words = 4
    max_words = 6

    try:
        num_words = int(input(f"Enter number of words in passphrase ({min_words}-{max_words} words): "))
        if num_words < min_words or num_words > max_words:
            raise ValueError(f"Number of words must be between {min_words} and {max_words}.")

        passphrase = generate_passphrase(num_words)
        print(f"Generated passphrase: {passphrase}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
