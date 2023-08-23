# Open the input and output files
with open('output.txt', 'r') as input_file, open('de_male_final.txt', 'w') as output_file:
    # Process each line in the input file
    for line in input_file:
        # Check if the line contains only a single letter
        if len(line.strip()) == 1 and line.strip().isalpha():
            continue  # Skip this line
        else:
            output_file.write(line)  # Write the line to the output file
