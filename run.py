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

        guessed_letters.append(user_input)

        if user_input not in word:
            attempts -= 1
            current_stage += 1  # Move to the next Hangman stage
            print(f"Wrong guess! {attempts} attempts left.")

        if current_stage == len(HANGMAN) - 1:
            print(HANGMAN[current_stage])
            print("Game over! You've been hanged.")
            break

    print(f"The word was: {word}")

# Function to display the rules


def display_rules():
    print("\nHangman Rules:")
    print("1. You have 60 seconds to guess the word.")
    print("2. You start with 6 attempts.")
    print("3. Guess one letter at a time.")
    print("4. If you guess a letter correctly, it will be revealed in the word.")
    print("5. If you guess a letter incorrectly, you lose an attempt.")
    print("6. You win the game if you guess the entire word.")
    print("7. You lose the game if you run out of time or attempts.")
    input("\nPress Enter to return to the main menu.")


# Main menu with options to view rules, play, or exit
menu = TerminalMenu(["View Rules", "Play Hangman", "Exit"])

# Display rules when the game starts
display_rules()

while True:
    choice_index = menu.show()
    if choice_index == 0:
        display_rules()
    elif choice_index == 1:
        play_hangman()
    elif choice_index == 2:
        print("Thanks for playing Hangman!")
        break
