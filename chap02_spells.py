# Impractical Python Code Chapter 2 (page 20-)

import string
my_whitespace = string.whitespace + '%'

# Printing the values
# for i in my_whitespace:
#     print(f'ord {ord(i)}: {i}')

fn = 'dictionaries/3of6all.txt'
# fn = 'dictionaries/american_words_short.txt'
# fn = 'dictionaries/american_words_long.txt'

palindromes = []

with open(fn) as f:
    line_count = 0
    line = f.readline()

    while line:
        word = line.strip()
        rword = "".join(reversed(word))
        if word == rword and len(word) > 1:
            palindromes.append(word)
        line_count += 1
        line = f.readline()

for i in palindromes:
    print(f'{i}')
print(f'{len(palindromes)} palindromes found in {line_count} words')

