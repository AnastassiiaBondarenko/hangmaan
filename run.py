import random
import gspread
from google.oauth2.service_account import Credentials
from simple_term_menu import TerminalMenu
from colorama import init, Fore, Back, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hang_maan')

PLAYER_DATA_SHEET = SHEET.worksheet('Hangman')

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

# Words for Hangman by difficulty level
word_lists = {
    "easy": ["cat", "dog", "sun", "hat", "red", "blue", "book", "tree", "lamp", "fish", "rose", "moon", "frog", "bear", "bird", "ship", "ball", "milk", "cake", "star", "corn", "leaf", "duck", "ring", "toys", "door", "gate", "bell", "desk", "film", "hair", "jump", "lake", "mask", "nest", "pill", "quilt", "rain", "sock", "tree", "vase", "wall", "zoo", "note", "ocean", "pencil", "queen", "radio", "snake", "table", "wheel"],
    "medium": ["flower", "banana", "happy", "dinner", "guitar", "jungle", "summer", "puzzle", "butter", "purple", "rocket", "orange", "camera", "pencil", "school", "monkey", "turtle", "holiday", "cherry", "shadow", "bicycle", "bouquet", "captain", "library", "helmet", "marble", "novelty", "opposite", "pleasant", "question", "resource", "electricity", "fantasy", "geometry", "horizon", "inspiration", "jewelry", "knowledge", "landscape", "mountain", "nightmare", "operation", "paradise", "quantity", "restaurant", "scientist", "technology", "umbrella", "vegetable", "waterfall", "xylophone", "yellow"],
    "hard": ["elephant", "chocolate", "television", "umbrella", "important", "celebration", "fantastic", "knowledge", "incredible", "tournament", "adventure", "opportunity", "mysterious", "vegetables", "experience", "leadership", "creativity", "recognition", "discovery", "architecture", "bureaucracy", "disproportionate", "encyclopedia", "hieroglyphics", "independence", "mathematician", "persuasiveness", "quantum mechanics", "syllabication", "bewildered", "exaggeration", "flamboyant", "gobbledygook", "hallucination", "incomprehensible", "jurisprudence", "kaleidoscope", "labyrinthine", "magnificence", "necessitarianism", "obliteration", "parapsychology", "quintessentially", "rambunctious", "simultaneously", "tintinnabulation", "ubiquitousness", "verisimilitude", "weltschmerz", "xerophthalmia", "youthfulness", "zeitgeist"]
}


# Initialize player's name and score
player_name = ""
score = 0

# Function to choose a random word from the word list based on difficulty


def choose_word(difficulty):
    words = word_lists[difficulty]
    return random.choice(words)

# Function to display the current state of the word with guessed letters


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += Fore.GREEN + letter + Fore.RESET
        else:
            display += Fore.YELLOW + "_" + Fore.RESET
    return display

# Function to update the score


def update_score(points):
    global score
    score += points

# Function to update the Google Sheet


def update_google_sheet(player_name, score):
    try:
        values_to_insert = [[player_name, str(score)]]
        PLAYER_DATA_SHEET.insert_rows(values_to_insert, 2)
    except Exception as e:
        print(f"Error updating Google Sheet: {str(e)}")


def reset_player_data():
    global player_name, score
    player_name = ""
    score = 0
# Function to play the Hangman game


def play_hangman(difficulty):
    global player_name, score
    word = choose_word(difficulty)
    guessed_letters = []
    attempts = 6
    current_stage = 0

    if not player_name:
        # Get the player's name if it's not already set
        while True:
            player_name = input(Fore.CYAN + "Enter your name: " + Fore.RESET)
            player_name = player_name.strip()
            if player_name and player_name.isalpha():
                player_name = player_name.capitalize()
                break
            else:
                print(Fore.RED + "Please enter a valid name." + Fore.RESET)

    while True:
        print(HANGMAN[current_stage])  # Display Hangman art
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(Fore.CYAN +
              f"Guessed letters: {', '.join(guessed_letters)}" + Fore.RESET)
        print(f"Attempts left: {attempts}")
        print(Fore.CYAN +
              f"Player: {player_name} | Current Score: {score}" + Fore.RESET)

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
            update_score(5)

        if current_stage == len(HANGMAN) - 1:
            print(HANGMAN[current_stage])
            print(Fore.WHITE + Back.RED + Style.BRIGHT +
                  "Game over! You've been hanged." + Fore.RESET + Back.RESET + Style.RESET_ALL)
            break

    print(Fore.CYAN + f"The word was: {word}" + Fore.RESET)

# Function to display the rules


def display_rules():
    title = "Hangman Rules:"
    rules_text = (
        "1. You have 6 attempts to guess the word. If you run out of attempts, the game is over.\n"
        "2. Guess one letter at a time by typing it in and pressing Enter.\n"
        "3. If you guess a letter correctly, it will be revealed in the word.\n"
        "4. If you guess a letter incorrectly, you lose an attempt.\n"
        "5. You win the game if you guess the entire word.\n"
        "6. The game offers three difficulty levels, each with different word lengths:\n"
        "   - Easy: Words are 3-4 letters long.\n"
        "   - Medium: Words are 5-7 letters long.\n"
        "   - Hard: Words are 9 letters or longer.\n\n"
        "To play, select a difficulty level from the main menu, and start guessing letters to uncover the hidden word. The game will adapt to your chosen difficulty, and your score will increase as you make correct guesses. Enjoy the game!"
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
        update_google_sheet(player_name, score)
        reset_player_data()
        break
