# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)


def counting_vowels_and_consonants(text: str) -> tuple[int, int]:

    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)


def average_vowels_and_consonants(paragraph: str) -> tuple[int, float, float]:
    """
    Calculates the average number of vowels and consonants per sentence in a paragraph.

    Args:
        paragraph: The input paragraph string.

    Returns:
        A tuple containing:
        (number of sentences, average vowels per sentence, average consonants per sentence)
    """

    sentences_raw = paragraph.replace('!', '.').replace('?', '.').split('.')
    
    sentences = [sentence for sentence in sentences_raw if sentence.strip()]
    
    num_sentences = len(sentences)
    if num_sentences == 0:
        return (0, 0.0, 0.0)

    total_vowels = 0
    total_consonants = 0

    for sentence in sentences:
        vowels, consonants = counting_vowels_and_consonants(sentence)
        total_vowels += vowels
        total_consonants += consonants

    avg_vowels = total_vowels / num_sentences
    avg_consonants = total_consonants / num_sentences

    return (num_sentences, avg_vowels, avg_consonants)

num_sentences, avg_vowels, avg_consonants = average_vowels_and_consonants(paragraph)

print("--- Paragraph Analysis ---")
print(f"The paragraph contains {num_sentences} sentences.")
print(f"On average, each sentence has {avg_vowels:.2f} vowels.")
print(f"On average, each sentence has {avg_consonants:.2f} consonants.")
