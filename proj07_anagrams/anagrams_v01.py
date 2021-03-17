"""
Solving Anagrams.

Created by: Tony Held
Created on: 2021-03-15

References & Acknowledgements:
1) Inspired by `Impractical Python Projects` Chapter 3

Notes
-----
1) multi word finder
2) select each letter,
    see if it is in the dict, if so process remainder
3) select two letters
"""
from collections import defaultdict, Counter
import random


def create_letter_counts(words):
    """Return of list of letter counts for each word in words"""
    letter_counts = [Counter(i) for i in words]
    return letter_counts

def load_dictionary(file_name):
    """load contents of text file into attribute self.words"""
    with open(file_name) as fn:
        words_raw = fn.readlines()
    words = [i.strip().lower() for i in words_raw]

    print(f'Dictionary with {len(words)} entries loaded.')
    print(f'The first and last 5 entries are:')
    print(f'{words[:5]}\n{words[-5:]}')

    return words

def listify_words(words):
    """Take a list of words and convert to a list of tuple of letters.
     The letters in the tuple are sorted alphabetically."""

    words_sorted = [tuple(sorted(i)) for i in words]

    print(f'\nThe first and last 5 entries are:')
    print(f'{words_sorted[:5]}\n{words_sorted[-5:]}')

    return words_sorted

def index_list(words):
    """Create a dictionary of occurrences of a list, and the frequency of each word, to speed up future searches.
    Returns
    -------
    dict_words - dict
        The key is the tuple of letters in a word,
        the value is the location(s) of that tuple in the original word list.
    frequencies - list
        list of frequencies of each word occurring in the word list

    """
    dict_words = defaultdict(list)

    for i, word in enumerate(words):
        dict_words[word].append(i)

    print(f'\nThe first 5 entries are:')
    for i, (k, v) in enumerate(dict_words.items()):
        if i > 5: break
        print(f'{k}: {v}')

    """Find the most n most frequently occurring words"""
    frequencies = sorted(dict_words.values(), key=lambda x: len(x), reverse=True)

    print(f'The 5 most frequent entries are:')
    print(f'{frequencies[:5]}')

    return dict_words, frequencies

def word1_contains_word2(word1, word2):
    """Based on letter frequency dictionaries created by collections.Counter,
    determine if word2 can be created by the letters in word1.

    Conceptually reads as word1.contains_word(word2) = True | False

    Notes
    -------
    1) collections.Counter behaves like a dictionary
    where the key is the letter and value is the frequency of the letter in the word.
    """
    # every letter in word2 appears with equal or greater frequency in word1.
    for k2, v2 in word2.items():
        if (k2 not in word1) or (v2 > word1[k2]):
            return False

    return True

def list_contains(word_list, letter_freq_list, single_word):
    """
    Find the members of the WordList that are contained in word.

    Parameters
    ----------
    word_list : list[str]
        list of words in plain text associated with letter_freq_list

    letter_freq_list : list[collections.Counter]
        list of word counters letter frequencies associated with WordList

    single_word : collections.Counter
        single word letter frequency

    Returns
    -------
    indices : list[int]
        indices of words that are contained in single word

    words : list[str]
        words that are contained in single_word
    """
    # indices = []
    # for i, e_word in enumerate(letter_freq_list):
    #     in_list = word1_contains_word2(word, e_word)
    #     if in_list is True:
    #         indices.append(i)

    indices = [i for i, e_word in enumerate(letter_freq_list)
               if word1_contains_word2(single_word, e_word) is True]

    words = [word_list[i] for i in indices]

    return indices, words

def remove_letters(word, letters):
    """
    Remove single occurrence of letter from word for each occurrence of letter in letters.
    """
    remaining_letters_list = list(word)
    for i in letters:
        remaining_letters_list.pop(remaining_letters_list.index(i))
    remaining_letters = "".join(remaining_letters_list)
    return remaining_letters, remaining_letters_list


class WordList:
    """Stores a list of words that are indexed and easy to search for anagrams"""

    def __init__(self, file_name):
        """file_name : location of file with a word list"""
        self.file_name = file_name
        self.words = load_dictionary(self.file_name)
        self.words_sorted = listify_words(self.words)
        self.words_indexed, self.frequencies = index_list(self.words_sorted)
        self.letter_counts = create_letter_counts(self.words)

    def print_most_frequent(self, n):
        print(f'\nThe {n} most frequently occurring anagrams in the word list are:')

        for words in self.frequencies[:n]:
            print(f'{len(words)} anagrams were found for these words:')
            for i in words:
                print(f'\t{self.words[i]}')

    def find_anagrams(self, word):
        """find the anagrams for a given word"""
        print(f'\nAnagrams for the word: {word}')
        word_sorted_tuple = tuple(sorted(word.strip().lower()))
        matches = self.words_indexed.get(word_sorted_tuple, [])
        if matches:
            for i, index in enumerate(matches):
                print(f'\t{i+1}) {self.words[index]}')
        else:
            print('\tWord not found in dictionary.')

    def find_contained(self, word):
        """Wrapper for list_contains"""
        indices, words = list_contains(self.words, self.letter_counts, Counter(word))
        return indices, words

    def input_loop(self, name):
        """Main loop to allow user to select anagram choices.
        Currently, it uses a random selection rather than console input.

        Returns
        -------
        name : str
            name that user input
        selected_words : list[str]
            list of words contained within name
        working_word : str
            letters that could not be used to form a word (empty if all letters are used)

        """
        selected_words = []

        print("Please enter your first and last name")
        # name = input()  # uncomment if you wish to have user input

        # extract only the letters from the name
        working_word = [i for i in name.lower() if i.isalpha()]

        while working_word:

            print(f'\nRemaining letters we have to work with: \n\t*{working_word}*')
            my_indices, my_words = self.find_contained(working_word)

            if not my_words:
                print('The remaining letters are exhausted or they do not contain possible words')
                break

            print('Possible words include')
            # show at max 25 words
            for i, word in enumerate(my_words[:25]):
                print(f'{i}), {word}')


            print("Please enter your choice")
            # choice = input()  # uncomment if you wish to have user input
            choice = random.choice(list(range(len(my_words))))

            print(f'You selected: {my_words[choice]}')
            selected_words.append(my_words[choice])
            working_word, _ = remove_letters(working_word, my_words[choice])

        return name, selected_words, working_word

    def user_interface(self, name='tony held'):
        """Point of entry for the anagram selection routines"""

        print('\nWelcome to the anagram creator!')

        name, selected_words, working_word = self.input_loop(name)

        print(f'\nYour name is: {name}')
        print(f'Phrase contained within your name: {selected_words}')

        if working_word:
            print(f'\nNote:  the following letters that remained that we could not form words from: '
                  f'\n\t{working_word}')




# def main():
file_name = 'dictionaries/2of4brif.txt'
words = WordList(file_name)
words.print_most_frequent(5)
words.find_anagrams('bear')
words.find_anagrams('polyglot')
words.find_anagrams('qwertyuiop')

words.user_interface('anthony edward held')
words.user_interface('ryan adamson meek')

# # find contained words
# search_word = 'tacotime'
# my_indices, my_words = words.find_contained(search_word)
# print(f'\nWords that can be found in {search_word}:\n{my_words}')


# if __name__ == '__main__':
#     main()
