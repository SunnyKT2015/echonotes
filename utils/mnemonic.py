import random

def generate_mnemonic(topics):
    """
    Generate mnemonic acronym and build a simple meaningful sentence
    where each word starts with the acronym letters.
    """

    if not topics:
        return {"acronym": "N/A", "phrase": "No topics available"}

    # Step 1: Acronym from topics
    letters = [t.strip()[0].upper() for t in topics if t.strip()]
    acronym = "".join(letters)

    # Step 2: Simple dictionary (common words per letter)
    simple_dict = {
        "A": ["Apple", "And", "Animals", "All"],
        "B": ["Boys", "Books", "Birds", "Beautiful"],
        "C": ["Cats", "Children", "Care", "Create"],
        "D": ["Dogs", "Doctors", "Data", "Drive"],
        "E": ["Everyone", "Energy", "Education", "Enjoy"],
        "F": ["Friends", "Family", "Food", "Fun"],
        "G": ["Girls", "Games", "Grow", "Good"],
        "H": ["Help", "Health", "Hope", "Happy"],
        "I": ["Ideas", "India", "Improve", "Innovate"],
        "J": ["Joy", "Jobs", "Join", "Journey"],
        "K": ["Knowledge", "Kids", "Keep", "Kind"],
        "L": ["Life", "Learn", "Love", "Leads"],
        "M": ["Man", "Mind", "Make", "Manage"],
        "N": ["Nature", "New", "Nice", "Needs"],
        "O": ["Open", "Our", "On", "Objects"],
        "P": ["People", "Peace", "Play", "Protect"],
        "Q": ["Quick", "Quality", "Queen", "Question"],
        "R": ["Run", "Read", "Research", "Real"],
        "S": ["Students", "Support", "Science", "Save"],
        "T": ["Time", "Teachers", "Think", "Together"],
        "U": ["Unity", "Use", "Under", "Understand"],
        "V": ["Value", "Voice", "Victory", "Very"],
        "W": ["Work", "World", "Win", "With"],
        "X": ["X-ray", "Xylophone", "Xenon"],  # fallback words
        "Y": ["You", "Youth", "Young", "Your"],
        "Z": ["Zoo", "Zero", "Zoom", "Zebra"],
    }

    # Step 3: Build sentence with random picks
    phrase_words = []
    for ch in acronym:
        if ch in simple_dict:
            phrase_words.append(random.choice(simple_dict[ch]))  # pick random word
        else:
            phrase_words.append(ch)

    phrase = " ".join(phrase_words)

    return {
        "acronym": acronym,
        "phrase": phrase
    }
