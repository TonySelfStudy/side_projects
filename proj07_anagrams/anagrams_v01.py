"""
Solving Anagrams.

Created by: Tony Held
Created on: 2021-03-15

References & Acknowledgements:
1) Inspired by `Impractical Python Projects` Chapter 3
"""
import collections

class word_list:
    """Stores a list of words that are indexed and easy to search for anagrams"""

    def __init__(self, file_name):
        """file_name : location of file with a word list"""
        self.file_name = file_name
        self.words = load_dictionary(self.file_name)
        self.words_sorted = listify_words(self.words)
        self.words_indexed, self.frequencies = index_list(self.words_sorted)

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
    dict_words = collections.defaultdict(list)

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


def main():
    file_name = 'dictionaries/2of4brif.txt'
    words = word_list(file_name)
    words.print_most_frequent(5)
    words.find_anagrams('bear')
    words.find_anagrams('polyglot')
    words.find_anagrams('qwertyuiop')

if __name__ == '__main__':
    main()
