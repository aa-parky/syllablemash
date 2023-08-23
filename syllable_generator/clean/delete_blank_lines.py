# Open the input and output files
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # Process each line in the input file
    for line in input_file:
        # Check if the line is blank (contains only whitespace characters)
        if line.strip():
            output_file.write(line)  # Write the line to the output file if it's not blank
