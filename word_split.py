import pyphen

# load a hyphenation dictionary for a specific library
dictionary = pyphen.Pyphen(lang='en_US')

# Hyphenate a word
word = "obstetrician"
hyphenated_word = dictionary.inserted(word, hyphen='-')

print(hyphenated_word)