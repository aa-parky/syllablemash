import random

# Read the list of words from the output.txt file
with open('latin_sounding_output.txt', 'r') as file:
    word_list = [line.strip() for line in file]

# Number of names to generate
num_names = 5

for _ in range(num_names):
    # Generate a random number between 1 and 3
    num_words = random.randint(1, 3)

    # Randomly select words from the list
    selected_words = random.sample(word_list, num_words)

    # Combine the words to form a name
    generated_name = ''.join(selected_words)

    # Capitalize only the first letter of the generated name
    capitalized_name = generated_name.capitalize()

    print("Generated Name:", capitalized_name)
