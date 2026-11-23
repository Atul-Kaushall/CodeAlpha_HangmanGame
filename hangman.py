import random

def play_hangman():
    # Predefined list of 5 words
    words = ["python", "developer", "algorithm", "database", "network"]
    secret_word = random.choice(words)
    
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print(f"You have {max_attempts} incorrect guesses allowed.\n")

    while incorrect_guesses < max_attempts:
        # Display current word progress
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("Word:", display_word.strip())
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
        
        # Check win condition
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word:", secret_word)
            return

        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.\n")

    print(f"Game Over! You ran out of guesses. The word was '{secret_word}'.")

if __name__ == "__main__":
    play_hangman()
