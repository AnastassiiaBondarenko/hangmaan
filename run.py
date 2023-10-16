import random
import time
import threading
import os
from simple_term_menu import TerminalMenu
from colorama import init, Fore, Back, Style

# Colorama
init(autoreset=True)


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

# Difficulty levels with  limits (in seconds)
difficulty_levels = {
    "easy": 60,
    "medium": 40,
    "hard": 20
}

# Function to choose a random word from the word list


def choose_word():
    return random.choice(word_list)

# Function to display the current state of the word with guessed letters


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += Fore.GREEN + letter
        else:
            display += Fore.YELLOW + "_"
    return display

# Function to clear the terminal screen


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Function to play the Hangman game


def play_hangman(difficulty):

    time_limit = difficulty_levels[difficulty]
    word = choose_word()
    guessed_letters = []
    attempts = 6
    current_stage = 0
    # User name input
    while True:
        player_name = input(Fore.CYAN + "Enter your name: ").strip().title()
        if (player_name.isalpha() and len(player_name) > 0):
            break
        else:
            print(
                Fore.RED + "Please enter a valid name with no numbers or special symbols.")

    game_start_time = time.time()

    # Timer thread to update the timer every second
    def timer_thread():
        while True:
            elapsed_time = int(time.time() - game_start_time)
            remaining_time = time_limit - elapsed_time
            print(Fore.MAGENTA +
                  f"Time remaining: {remaining_time} seconds", end="\n")
            if remaining_time <= 0:
                # Move to a new line when the game ends
                print(Fore.RED + "Time's up! You ran out of time.", end="\n")
                break
            time.sleep(1)

    timer = threading.Thread(target=timer_thread)
    timer.daemon = True
    timer.start()

    while True:
        print(HANGMAN[current_stage])  # Display Hangman art
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(Fore.CYAN + f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

        if "_" not in display_word(word, guessed_letters):
            game_duration = int(time.time() - game_start_time)
            print(
                Fore.GREEN + f"Congratulations, {player_name}! You guessed the word in {game_duration} seconds.")
            break

        if attempts <= 0:
            print(HANGMAN[len(HANGMAN) - 1])
            print(Fore.RED + "Game over! You're out of attempts.")
            break

        user_input = input(
            Fore.YELLOW + "Guess a letter (or 'Q' to quit): ").lower()

        if user_input == 'q':
            print(Fore.YELLOW + "You quit the game.")
            break

        if len(user_input) != 1:
            print(Fore.RED + "Please enter only one character.")
            continue

        if not user_input.isalpha():
            print(Fore.RED + "Please enter a letter, not a number or special character.")
            continue

        if user_input in guessed_letters:
            print(Fore.RED + "You've already guessed that letter.")
            continue

        guessed_letters.append(user_input)

        if user_input not in word:
            attempts -= 1
            current_stage += 1
            print(Fore.RED + f"Wrong guess! {attempts} attempts left.")

        if current_stage == len(HANGMAN) - 1:
            print(HANGMAN[current_stage])
            print(Fore.WHITE + Back.RED + Style.BRIGHT +
                  "Game over! You've been hanged.")
            break

    print(Fore.CYAN + Back.LIGHTMAGENTA_EX +
          Style.BRIGHT + f"The word was: {word}")

# Function to display the rules


def display_rules():
    title = "Hangman Rules:"
    rules_text = (
        "1. You have a limited time to guess the word based on the difficulty level:\n"
        "   - Easy: 60 seconds\n"
        "   - Medium: 40 seconds\n"
        "   - Hard: 20 seconds\n"
        "2. You start with 6 attempts.\n"
        "3. Guess one letter at a time.\n"
        "4. If you guess a letter correctly, it will be revealed in the word.\n"
        "5. If you guess a letter incorrectly, you lose an attempt.\n"
        "6. You win the game if you guess the entire word.\n"
        "7. You lose the game if you run out of time or attempts."
    )

    colored_title = f"{Fore.MAGENTA}{title}"
    colored_rules_text = f"{Fore.CYAN}{rules_text}"

    print(f"{colored_title}\n{colored_rules_text}")
    input(f"{Fore.GREEN}{Back.LIGHTYELLOW_EX}{Style.BRIGHT}\nPress Enter to return to the main menu.")


# Main menu with options to view rules, play, or exit

menu = TerminalMenu(
    [
        f"View Rules",
        f"Play Easy",
        f"Play Medium",
        f"Play Hard",
        f"Exit"
    ]
)
# Display rules when the game starts
display_rules()

while True:
    choice_index = menu.show()
    if choice_index == 0:
        display_rules()
    elif choice_index == 1:
        play_hangman("easy")
    elif choice_index == 2:
        play_hangman("medium")
    elif choice_index == 3:
        play_hangman("hard")
    elif choice_index == 4:
        print(Fore.CYAN + Back.MAGENTA + Style.BRIGHT +
              "Thanks for playing Hangman!")
        break
clear_screen()
