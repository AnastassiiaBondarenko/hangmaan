import random
import time
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


# Difficulty levels with time limits (in seconds)
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
            display += Fore.GREEN + letter + Fore.RESET
        else:
            display += Fore.YELLOW + "_" + Fore.RESET
    return display


score = 0


# Function to update the score
def update_score(score, points):
    return score + points

# Function to play the Hangman game


def play_hangman(difficulty):
    global score
    time_limit = difficulty_levels[difficulty]
    word = choose_word()
    guessed_letters = []
    attempts = 6
    current_stage = 0
    start_time = time.time()
# Player name input
    while True:
        player_name = input(Fore.CYAN + "Enter your name: " + Fore.RESET)
        player_name = player_name.strip()

        if player_name and player_name.isalpha():
            player_name = player_name.capitalize()
            break
        else:
            print(Fore.RED + "Please enter a valid name." + Fore.RESET)

    while True:
        elapsed_time = int(time.time() - start_time)
        remaining_time = time_limit - elapsed_time
        if remaining_time <= 0:
            print(Fore.RED + "Time's up! You ran out of time." + Fore.RESET)
            break

        print(HANGMAN[current_stage])  # Display Hangman art
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(Fore.CYAN +
              f"Guessed letters: {', '.join(guessed_letters)}" + Fore.RESET)
        print(f"Attempts left: {attempts}")
        print(Fore.MAGENTA +
              f"Time remaining: {remaining_time} seconds" + Fore.RESET)
        print(Fore.CYAN + f"Player: {player_name} | Current Score: {score}")
        if "_" not in display_word(word, guessed_letters):
            print(Fore.GREEN + "Congratulations! You guessed the word." + Fore.RESET)
            break
        if attempts <= 0:
            print(HANGMAN[len(HANGMAN) - 1])
            print(Fore.RED + "Game over! You're out of attempts." + Fore.RESET)
            break

        user_input = input(
            Fore.YELLOW + "Guess a letter (or 'Q' to quit): " + Fore.RESET).lower()

        if user_input == 'q':
            print(Fore.YELLOW + "You quit the game." + Fore.RESET)
            break

        if len(user_input) != 1:
            print(Fore.RED + "Please enter only one character." + Fore.RESET)
            continue

        if not user_input.isalpha():
            print(
                Fore.RED + "Please enter a letter, not a number or special character." + Fore.RESET)
            continue

        if user_input in guessed_letters:
            print(Fore.RED + "You've already guessed that letter." + Fore.RESET)
            continue

        guessed_letters.append(user_input)

        if user_input not in word:
            attempts -= 1
            current_stage += 1
            print(
                Fore.RED + f"Wrong guess! {attempts} attempts left." + Fore.RESET)
        else:
            score = update_score(score, 5)

        if current_stage == len(HANGMAN) - 1:
            print(HANGMAN[current_stage])
            print(Fore.WHITE + Back.RED + Style.BRIGHT +
                  "Game over! You've been hanged." + Fore.RESET + Back.RESET + Style.RESET_ALL)
            break

    print(Fore.CYAN + f"The word was: {word}" + Fore.RESET)
    print(Fore.BLUE + f"Your final score is: {score}")
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

    colored_title = f"{Fore.MAGENTA}{title}{Fore.RESET}"
    colored_rules_text = f"{Fore.CYAN}{rules_text}{Fore.RESET}"

    print(f"{colored_title}\n{colored_rules_text}")
    input(f"{Fore.GREEN}{Back.LIGHTYELLOW_EX     }{Style.BRIGHT}\nPress Enter to return to the main menu.{Style.RESET_ALL}{Back.RESET}{Fore.RESET}")


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
              "Thanks for playing Hangman!" + Style.RESET_ALL + Fore.RESET + Back.RESET)
        break
