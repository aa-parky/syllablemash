import nltk
nltk.download('names')  # Download the names dataset

from nltk.corpus import names

# Load the German male names
german_male_names = names.words('male.txt')

# Write the German male names to a file
with open('de_male.txt', 'w') as file:
    for name in german_male_names:
        file.write(name + '\n')

print("German male names written to de_male.txt")
