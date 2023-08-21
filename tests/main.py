import nltk
from nltk.corpus import cmudict
nltk.download('cmudict')

pronouncing_dict = cmudict.dict()

def separate_syllables(sepsy):
    if sepsy.lower() in pronouncing_dict:
        syllables_list = [y[:-1] for x in pronouncing_dict[sepsy.lower()] for y in x if y[-1].isdigit() or y[-1] == '']
        return syllables_list
    else:
        return []

text = "this is a test of counting syllables, a very simple test"
words = text.split()

for word in words:
    syllables = separate_syllables(word)
    syllable_splits = [s[:-1] for s in syllables]
    num_syllables = len(syllable_splits)
    print(f"Word: {word}, Syllable Splits: {', '.join(syllable_splits)}, Number of Syllables: {num_syllables}")
