import random
import datetime

# Read the list of words from the output.txt file
with open('polish_sounding_output.txt', 'r') as file:
    word_list = [line.strip() for line in file]

# Number of names to generate
num_names = 5

generated_names = []  # To store the generated names

for _ in range(num_names):
    # Generate a random number between 1 and 3
    num_words = random.randint(1, 3)

    # Randomly select words from the list
    selected_words = random.sample(word_list, num_words)

    # Combine the words to form a name
    generated_name = ''.join(selected_words)

    # Capitalize only the first letter of the generated name
    capitalized_name = generated_name.capitalize()

    generated_names.append(capitalized_name)  # Store the generated name

    print("Generated Name:", capitalized_name)

# Create a filename based on date and time
current_datetime = datetime.datetime.now()
filename = current_datetime.strftime("%Y-%m-%d_%H-%M-%S") + "_generated_names.txt"

# Write the generated names to the file
with open(filename, 'w') as output_file:
    for name in generated_names:
        output_file.write(name + '\n')

print("Generated names have been saved to:", filename)
