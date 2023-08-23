import re

# Open the input and output files
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # Process each line in the input file
    for line in input_file:
        # Use regular expression to remove non-letter characters
        processed_line = re.sub(r'[^a-zA-Z\n]', '', line)

        # Write the processed line to the output file
        output_file.write(processed_line)
