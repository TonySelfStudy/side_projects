"""
Letter usage histogram to plot a poor man's bar chart of letter frequency in a sentence.

Created by: Tony Held
Created on: 2021-03-06

References & Acknowledgements:
    1) Inspired by `Impractical Python Projects` chapter 1 challenge
"""
import pprint
pp = pprint.PrettyPrinter(indent=4, width=200)  # usage pp(stuff)


class LetterHistogram:
    def __init__(self, sentence):
        self.sentence = sentence.lower()
        self.initialize_dict()
        self.populate_dict()

    def initialize_dict(self):
        """initialize dictionary with english letters"""
        num_letters = 26
        first_letter = ord("a")
        letters = {chr(i): [] for i in range(first_letter, first_letter + num_letters)}
        self.freq_dict = letters

    def populate_dict(self):
        """populate the ordered dict"""
        for c in self.sentence:
            # only add letters to frequency distribution
            if c in self.freq_dict:
                self.freq_dict[c].append(c)

    def print_dict(self):
        print(f'\nOriginal sentence: \n{self.sentence}')
        pp.pprint(self.freq_dict)


if __name__ == '__main__':
    sentence1 = "Like the castle in its corner in a medieval game, " \
                "I foresee terrible trouble and I stay here just the same"
    lh_1 = LetterHistogram(sentence1)
    lh_1.print_dict()
