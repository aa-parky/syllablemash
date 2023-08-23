import nltk
nltk.download('names')  # Download the names dataset

from nltk.corpus import names

# Load the German female names
german_female_names = names.words('female.txt')

# Write the German female names to a file
with open('de_fem.txt', 'w') as file:
    for name in german_female_names:
        file.write(name + '\n')

print("German female names written to de_fem.txt")
