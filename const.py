
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
