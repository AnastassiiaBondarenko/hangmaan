from colorama import Fore, Back, Style

# Hangman art stages
HANGMAN = (
    f"""{Fore.GREEN}
    ------
    |    |
    |
    |
    |
    |
    |
    ----------{Fore.RESET}
    """,
    f"""{Fore.LIGHTYELLOW_EX}
    ------
    |    |
    |    O
    |
    |
    |
    |
    ----------{Fore.RESET}
    """,
    f"""{Fore.YELLOW}
    ------
    |    |
    |    O
    |    |
    |
    |
    |
    ----------{Fore.RESET}
    """,
    f"""{Fore.LIGHTBLUE_EX}
    ------
    |    |
    |    O
    |    |\\
    |
    |
    |
    ----------{Fore.RESET}
    """,
    f"""{Fore.BLUE}
    ------
    |    |
    |    O
    |   /|\\
    |
    |
    |
    ----------{Fore.RESET}
    """,
    f"""{Fore.LIGHTRED_EX}
    ------
    |    |
    |    O
    |   /|\\
    |   /
    |
    |
    ----------{Fore.RESET}
    """,
    f"""{Fore.RED}
    ------
    |    |
    |    O
    |   /|\\
    |   / \\
    |
    |
    ----------{Fore.RESET}
    """
)


# Words for Hangman by difficulty level
word_lists = {
    "easy": [
        "cat",
        "dog",
        "sun",
        "hat",
        "red",
        "blue",
        "book",
        "tree",
        "lamp",
        "fish",
        "rose",
        "moon",
        "frog",
        "bear",
        "bird",
        "ship",
        "ball",
        "milk",
        "cake",
        "star",
        "corn",
        "leaf",
        "duck",
        "ring",
        "toys",
        "door",
        "gate",
        "bell",
        "desk",
        "film",
        "hair",
        "jump",
        "lake",
        "mask",
        "nest",
        "pill",
        "quilt",
        "rain",
        "sock",
        "tree",
        "vase",
        "wall",
        "zoo",
        "note",
        "ocean",
        "pencil",
        "queen",
        "radio",
        "snake",
        "table",
        "wheel"
    ],
    "medium": [
        "flower",
        "banana",
        "happy",
        "dinner",
        "guitar",
        "jungle",
        "summer",
        "puzzle",
        "butter",
        "purple",
        "rocket",
        "orange",
        "camera",
        "pencil",
        "school",
        "monkey",
        "turtle",
        "holiday",
        "cherry",
        "shadow",
        "bicycle",
        "bouquet",
        "captain",
        "library",
        "helmet",
        "marble",
        "novelty",
        "opposite",
        "pleasant",
        "question",
        "resource",
        "fantasy",
        "geometry",
        "horizon",
        "jewelry",
        "knowledge",
        "landscape",
        "mountain",
        "nightmare",
        "operation",
        "paradise",
        "quantity",
        "restaurant",
        "scientist",
        "technology",
        "umbrella",
        "vegetable",
        "waterfall",
        "xylophone",
        "yellow"
    ],
    "hard": [
        "elephant",
        "chocolate",
        "television",
        "umbrella",
        "important",
        "celebration",
        "fantastic",
        "knowledge",
        "incredible",
        "tournament",
        "adventure",
        "opportunity",
        "mysterious",
        "vegetables",
        "experience",
        "leadership",
        "creativity",
        "recognition",
        "discovery",
        "architecture",
        "bureaucracy",
        "disproportionate",
        "encyclopedia",
        "electricity",
        "hieroglyphics",
        "inspiration",
        "independence",
        "mathematician",
        "persuasiveness",
        "quantummechanics",
        "syllabication",
        "bewildered",
        "exaggeration",
        "flamboyant",
        "gobbledygook",
        "hallucination",
        "incomprehensible",
        "jurisprudence",
        "kaleidoscope",
        "labyrinthine",
        "magnificence",
        "necessitarianism",
        "obliteration",
        "parapsychology",
        "quintessentially",
        "rambunctious",
        "simultaneously",
        "tintinnabulation",
        "ubiquitousness",
        "verisimilitude",
        "weltschmerz",
        "xerophthalmia",
        "youthfulness",
        "zeitgeist"
    ]
}
