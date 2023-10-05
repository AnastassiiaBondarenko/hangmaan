import random
import time
from simple_term_menu import TerminalMenu

# Hangman art stages
HANGMAN = (
    """
    ------
    |    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |    |\\
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |   / 
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |   /|\\
    |   / \\
    |
    ----------
    """
)

# List of words for the Hangman game
word_list = ["cat", "dog", "gallery", "balloon", "heart", "love", "sunset", "instagram", "black", "flowers",
             "energy", "wedding", "fruits", "developer", "summer", "spain", "vacation"]

# Function to choose a random word from the word list


def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word with guessed letters


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to play the Hangman game


def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    current_stage = 0
    start_time = time.time()

    while True:
        elapsed_time = int(time.time() - start_time)
        remaining_time = 60 - elapsed_time
        if remaining_time <= 0:
            print("Time's up! You ran out of time.")
            break

        print(HANGMAN[current_stage])  # Display Hangman art
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")
        print(f"Time remaining: {remaining_time} seconds")

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word.")
            break
        if attempts <= 0:
            print(HANGMAN[len(HANGMAN) - 1])
            print("Game over! You're out of attempts.")
            break

        user_input = input("Guess a letter (or 'Q' to quit): ").lower()

        if user_input == 'q':
            print("You quit the game.")
            break

        if len(user_input) != 1 or not user_input.isalpha():
            print("Please enter a valid single letter.")
            continue

        if user_input in guessed_letters:
            print("You've already guessed that letter.")
            continue
