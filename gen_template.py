import os


def main():
    # Get user input for the directory name (without "_sounding")
    dir_name = input("Enter the name for the directory: ")

    # Add "_sounding" to the end of the directory name
    dir_name += "_sounding"

    # Remove any invalid characters from the directory name
    dir_name = sanitize_dir_name(dir_name)

    # Create the directory
    try:
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created successfully!")

        # Create input and output files
        create_files(dir_name)

    except OSError:
        print(f"Error creating directory '{dir_name}'.")


def sanitize_dir_name(name):
    # Replace invalid characters with underscores
    valid_chars = "-_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    sanitized_name = ''.join(c if c in valid_chars else '_' for c in name)
    return sanitized_name


def create_files(directory):
    # File names
    input_file_name = directory + "_input.txt"
    output_file_name = directory + "_output.txt"
    name_generator = directory + "_name_generator.py"
    paragraph_hyphenator = directory + "_paragraph_hyphenator.py"

    try:
        # Create empty input file
        with open(os.path.join(directory, input_file_name), 'w') as input_file:
            pass

        # Create empty output file
        with open(os.path.join(directory, output_file_name), 'w') as output_file:
            pass

        # Create empty name generator file
        with open(os.path.join(directory, name_generator), 'w') as name_gen_file:
            pass

        # Read the paragraph_hyphenator template file
        with open('paragraph_hyphenator_template.py', 'r') as template_file:
            template_content = template_file.read()

        # Replace occurrences of 'COUNTRY' with dir_name
        modified_content = template_content.replace('COUNTRY', directory)

        # Create paragraph hyphenator file with modified content
        with open(os.path.join(directory, paragraph_hyphenator), 'w') as para_hyphenator_file:
            para_hyphenator_file.write(modified_content)

        print(f"Empty input, output, name generator, and paragraph hyphenator files created successfully!")
    except IOError:
        print("Error creating files.")


if __name__ == "__main__":
    main()
