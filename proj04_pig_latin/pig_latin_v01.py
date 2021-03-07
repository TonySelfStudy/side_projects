"""
Pig latin translation tool.

Created by: Tony Held
Created on: 2021-03-06

The phrase:         "Speaking Pig Latin does not make one porcine!"
Is translated to:   "Eakingspay Igpay Atinlay oesday otnay akemay oneway orcinepay!"

Implementation Details:
1. Words that start with a consonant have all consonant letters up to the first vowel moved
    to the end of the word, and "AY" is appended to the word's end.
2. Words that start with a vowel (A, E, I, O, U), or those that have no vowels,
    have "WAY" appended to the word's end.
3. If no vowels are in a word, the first 'y' is considered a vowel if present.
4. If the letter q is to be moved, it's following 'u' will be moved too if present.

Subtleties not implemented:
1. Pig latin is based on how a word sounds, not how it is spelled.
    In this implementation, translations are made strictly from a words spelling.
    For example, "one" should be treated as "won" if using your ear and would be
    best translated as onway rather than oneway.
2. Compound words should be broken up piecemeal and translated separately to make Pig Latin less obvious.
    However, in this implementation, compound words are considered a single word.
    For instance: "mudslide" is translated to udslidemay.  It would be superior
    to change it to "mud slide" first and then translate it as "udmay ideslay" to make it harder for those
    who don't know pig latin to decode what you are saying.

References & Acknowledgements:
    1) Inspired by `Impractical Python Projects` chapter 1 challenge
"""
import argparse


class PigLatin:
    # Store the letters, consonants, and vowels, etc,
    # as sets at the class-level
    # -----------------------------------------
    num_letters = 26
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    upper_case_first = ord("A")     # ord is the integer representing a character
    lower_case_first = ord("a")
    lower_case = {chr(i) for i in range(lower_case_first, lower_case_first + num_letters)}
    upper_case = {chr(i) for i in range(upper_case_first, upper_case_first + num_letters)}
    letters = lower_case | upper_case
    consonants = letters.difference(vowels)

    ignored_chars = {"'"}   # These characters should be stripped from the PLS (pig latin structure) :)

    A = list(letters);      A.sort()        # All letters
    C = list(consonants);   C.sort()        # All consonants
    V = list(vowels);       V.sort()        # All vowels (excluding the letter y)

    def __init__(self, original_text):
        self.original_text = original_text      # Text to be translated
        self.translated_text = []               # Translated text
        self.current_word = []                  # Current working word being processed to pig latin

    def pig_sentence(self):
        """Translate sentence to pig latin.
        1.  Skip ignored characters.
        2.  If you find a letter, add it to the current word.
        3.  If you find a non-letter, translate the current word (if it exists) and place it
            in the translated text followed by the non-letter.
        """
        for c in self.original_text:
            # Skip ignored characters
            if c in PigLatin.ignored_chars:
                continue
            # If you get a non-letter, translate the current word (if it exists) then add the non-letter
            if c not in PigLatin.A:
                self.pig_word()
                self.translated_text.append(c)
            # Otherwise add the letter to the current word
            else:
                self.current_word.append(c)

        # In case the sentence did not end in a non-letter (e.g. punctuation), run pig_word again
        self.pig_word()
        # Convert the list of translated text into a single string
        self.translated_text = ''.join(self.translated_text)

    def pig_word(self):
        """Translate a single word to pig latin."""

        # If the working word is empty, return without modifying the translation
        if not self.current_word:
            return

        # Initialize local variables
        first_vowel = None
        first_qu = None
        first_y = None
        is_cap = False
        return_word = ""

        # Convert working word to a string and save it's capitalization
        word = ''.join(self.current_word)
        if word[0] in PigLatin.upper_case:
            is_cap = True

        # Find the first occurrence of a vowel, qu, and y
        for i in PigLatin.V:
            result = word.find(i)
            if result != -1:
                if first_vowel is None:
                    first_vowel = result
                else:
                    if result < first_vowel:
                        first_vowel = result

        result = word.find('qu')
        first_qu = result if result != 1 else None

        result = word.find('y')
        first_y = result if result != 1 else None

        # If no other vowels present, assume the first y is a vowel sound
        if first_vowel is None:
            first_vowel = first_y

        # Determine translated word
        if first_qu >= 0 and first_qu == (first_vowel - 1):       # First vowel is part of a qu
            return_word = word[first_qu+2:] + word[0:first_qu+2] + 'ay'
        elif first_vowel <= 0 or first_vowel is None:           # Starts with a vowel or has no vowel
                return_word = word + 'way'
        else:                                                   # Starts with a non-q consonant
            return_word = word[first_vowel:] + word[0:first_vowel] + 'ay'

        # Reset capitalization
        if is_cap:
            return_word = return_word.capitalize()
        else:
            return_word = return_word.lower()

        # print(word, return_word, first_vowel, first_y, first_qu, )

        # Add translated word to sentence and reset current word buffer
        self.translated_text.append(return_word)
        self.current_word = []

def sample_translation():
    text = "Speaking Pig Latin does not make one porcine!"
    print(f'Translating to pig latin: {text}')
    translator = PigLatin(text)
    translator.pig_sentence()
    print(translator.translated_text)


if __name__ == '__main__':

    # If true, run main via the command line input
    command_line_mode = True

    if command_line_mode:
        # command line parameters
        parser = argparse.ArgumentParser(description='Pig latin translator')
        parser.add_argument('text', help="quoted string of text you wish to translate")
        args = parser.parse_args()

        y = PigLatin(args.text)
        y.pig_sentence()
        print(y.translated_text)
    else:
        sample_translation()
