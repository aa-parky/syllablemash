# Open the input and output files
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # Process each line in the input file
    for line in input_file:
        # Convert the line to lowercase
        processed_line = line.lower()

        # Write the processed line to the output file
        output_file.write(processed_line)
