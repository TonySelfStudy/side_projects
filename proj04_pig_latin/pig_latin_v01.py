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
    # Store the letters, consonants, and vowels, and symbols to ignore,
    # at the class-level
    # -----------------------------------------
    num_letters = 26
    lower_case = {chr(i) for i in range(ord("a"), ord("a") + num_letters)}
    upper_case = {chr(i) for i in range(ord("A"), ord("A") + num_letters)}
    letters = lower_case | upper_case
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    consonants = letters.difference(vowels)

    A = list(letters);      A.sort()        # All letters
    C = list(consonants);   C.sort()        # All consonants
    V = list(vowels);       V.sort()        # All vowels (excluding the letter y)

    # ignored_chars are characters that should be stripped
    # from the PLS (pig latin structure) :)
    ignored_chars = {"'"}

    def __init__(self, original_text):
        self.original_text = original_text                                  # Text to be translated
        print(f'Translating to Pig Latin: {self.original_text}')
        self.translated_text = PigLatin.pig_sentence(self.original_text)    # Translated text
        print(f'Translated text: {self.translated_text}')

    @staticmethod
    def pig_sentence(sentence):
        """Translate sentence to pig latin.

        Parameters
        ----------
        sentence : str
            Sentence to translate.

        Returns
        -------
        translated_text : str
            Pig latin translation of sentence

        Methodology
        ------------
        1.  Skip ignored characters.
        2.  If you find a letter, add it to the current word.
        3.  If you find a non-letter, translate the current word (if it exists) and place it
            in the translated text followed by the non-letter.
        """
        current_word = ""
        translated_text = []

        for c in sentence:
            # Skip ignored characters
            if c in PigLatin.ignored_chars:
                continue

            # If you get a non-letter
            #   1) translate the current word (if it exists)
            #   2) add the the non-letter to translated text
            #   3) reset current word
            if c not in PigLatin.A:
                if current_word:
                    translated_text.append(PigLatin.pig_word(current_word))
                translated_text.append(c)
                current_word = ""

            # Otherwise add the letter to the current word
            else:
                current_word += c

        # In case the sentence did not end in a non-letter (e.g. punctuation), run pig_word again
        if current_word:
            translated_text.append(PigLatin.pig_word(current_word))

        # Convert the list of translated text into a single string
        translated_text = ''.join(translated_text)

        return translated_text

    @ staticmethod
    def pig_word(word):
        """Translate a single word to pig latin.

        Parameters
        ----------
        word : str
            Word to translate.  Assumed to be free of special characters.

        Returns
        -------
        pig_word : str
            Pig latin translation of word
        """
        # Initialize return word
        pig_word = ""

        # If the requested word is empty, return empty string
        if not word:
            return pig_word

        # Save capitalization of first letter
        if word[0] in PigLatin.upper_case:
            is_cap = True
        else:
            is_cap = False

        # Find the first occurrence of a regular vowel
        first_regular_vowel = None
        vowel_locations = [word.find(i) for i in PigLatin.V]      # will return -1 if not found
        vowel_locations = [i for i in vowel_locations if i >= 0]  # remove -1's from list
        if vowel_locations:
            first_regular_vowel = min(vowel_locations)

        # Find first 'y'
        result = word.find('y')
        if result == -1:
            first_y = None
        else:
            first_y = result

        # Determine first vowel.
        # If no regular vowels, assume the first y is a vowel sound.
        if first_regular_vowel:
            first_vowel = first_regular_vowel
        else:
            first_vowel = first_y

        # Find first 'qu' sequence.
        # If the u in qu is the first vowel, it needs special handling.
        result = word.find('qu')
        if result == -1:
            first_qu = None
        else:
            first_qu = result

        # Determine translated word
        # -------------------------
        # Special Case - first vowel is part of a qu
        if (first_qu is not None) and (first_qu < first_vowel):
            pig_word = word[first_qu+2:] + word[0:first_qu+2] + 'ay'
        # Has no vowel or starts with a vowel
        elif (first_vowel is None) or (first_vowel == 0):
            pig_word = word + 'way'
        # Starts with a non-q consonant
        else:
            pig_word = word[first_vowel:] + word[0:first_vowel] + 'ay'

        # Reset capitalization
        if is_cap:
            pig_word = pig_word.capitalize()
        else:
            pig_word = pig_word.lower()

        return pig_word


if __name__ == '__main__':

    try:
        # determine command line parameters
        parser = argparse.ArgumentParser(description='Pig latin translator')
        parser.add_argument('text', help="quoted string of text you wish to translate")
        args = parser.parse_args()
        text_to_translate = args.text
    except:
        print('Argument not passed via command line')
        print('Using default sentence for example translation')
        text_to_translate = "Speaking Pig Latin does not make one porcine!"

    translation = PigLatin(text_to_translate)
