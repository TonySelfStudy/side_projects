"""
Finding palindromes/palingrams in dictionaries.

Created by: Tony Held
Created on: 2021-03-15

References & Acknowledgements:
1) Inspired by `Impractical Python Projects` chapter 2
"""
import time


def load_dictionary():
    file_name = 'dictionaries/12dicts-6.0.2/International/2of4brif.txt'

    with open(file_name) as fn:
        words_raw = fn.readlines()
    words = [i.strip().lower() for i in words_raw]

    print(f'Dictionary with {len(words)} entries loaded.')
    print(f'The first and last 5 entries are:')
    print(f'{words[0:5]}\n{words[-5:]}')

    return words


def find_palindromes(words):
    # reverse letters in all words
    r_words = [i[::-1] for i in words];

    # find palindromes in dictionary
    palindromes = [i for i, j in zip(words, r_words) if i == j]
    print(f'{len(palindromes)} palindromes detected. The are: \n{palindromes}')


def find_palingrams(words, run_mode):
    """Find dictionary palingrams.
        run_mode = 'sets' | 'lists'
    """
    print(f'Finding palingrams using {run_mode}.')
    time_start1 = time.time()

    if run_mode == 'sets':
        words = set(words)

    pali_list = []
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end - i:] in words:
                    pali_list.append((word, rev_word[end - i:]))
                if word[:i] == rev_word[end - i:] and rev_word[:end - i] in words:
                    pali_list.append((rev_word[:end - i], word))

    # sort palingrams on first word
    palingrams_sorted = sorted(pali_list)

    time_end1 = time.time()
    time_diff1 = time_end1 - time_start1
    print(f'Simulation using {run_mode} complete in {time_diff1} seconds.')

    # display list of palingrams
    print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
    for first, second in palingrams_sorted:
        print("{} {}".format(first, second))

    return palingrams_sorted

def main():
    words = load_dictionary()
    find_palindromes(words)

    # Determine if you wish to run the palingrams using lists or sets
    run_modes = ['sets', 'lists']

    find_palingrams(words, run_modes[0])
    # find_palingrams(words, run_modes[1])


if __name__ == '__main__':
    main()
