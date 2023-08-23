import re
from collections import Counter
from nltk.corpus import cmudict

# Load the CMU Pronouncing Dictionary
pronouncing_dict = cmudict.dict()

def count_syllables(word):
    if word.lower() in pronouncing_dict:
        return max([len(list(y for y in x if y[-1].isdigit())) for x in pronouncing_dict[word.lower()]])
    else:
        return None

def get_syllables(word):
    if word.lower() in pronouncing_dict:
        return [y for x in pronouncing_dict[word.lower()] for y in x]
    else:
        return []

def main():
    input_file_path = "de_fem.txt"
    output_file_path = "de_fem_syllables.txt"

    # Read the input file
    with open(input_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text)  # Tokenize words

    syllable_counter = Counter()
    total_words = len(words)

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        print("Syllable\tFrequency\tPercentage")
        output_file.write("Syllable\tFrequency\tPercentage\n")
        for word in words:
            syllables = get_syllables(word)
            if syllables:
                syllable_count = len(syllables)
                syllable_counter[syllable_count] += 1
                percentage = (1 / total_words) * 100
                print(f"{', '.join(syllables)}\t{syllable_count}\t{percentage:.2f}%")
                output_file.write(f"{', '.join(syllables)}\t{syllable_count}\t{percentage:.2f}%\n")

if __name__ == "__main__":
    main()
