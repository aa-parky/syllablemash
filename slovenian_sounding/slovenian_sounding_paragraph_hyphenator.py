import pyphen
import re

# Load a hyphenation dictionary for a specific language
dictionary = pyphen.Pyphen(lang='en_En')


def hyphenate_paragraph(paragraph):
    # Tokenize the paragraph into words
    words = re.findall(r'\b\w+\b', paragraph)

    # Hyphenate each word and store the hyphenated words in a list
    hyphenated_words = []
    for word in words:
        hyphenated_word = dictionary.inserted(word, hyphen='-')
        if hyphenated_word != word:
            hyphenated_words.append(hyphenated_word)

    return hyphenated_words


# Read the text from the file "input.txt"
with open("slovenian_sounding_input.txt", "r") as file:
    input_text = file.read()

hyphenated_word_list = hyphenate_paragraph(input_text)

# Print the hyphenated word list
print(hyphenated_word_list)

# Save the hyphenated word list to the file "output.txt"
with open("slovenian_sounding_output.txt", "w") as file:
    for word in hyphenated_word_list:
        file.write(word + '\n')

# Read the content from the file "output.txt"
with open("slovenian_sounding_output.txt", "r") as file:
    content = file.read()

# Replace hyphens with new lines and remove hyphens
modified_content = re.sub(r'-', '\n', content)

# Write the modified content back to the file "output.txt"
with open("slovenian_sounding_output.txt", "w") as file:
    file.write(modified_content)