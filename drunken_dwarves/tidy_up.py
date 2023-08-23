import re


def clean_text(text):
    # Remove all non-letter characters using regex
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text


def create_word_list(text):
    # Split the cleaned text into words and create a list
    word_list = text.split()
    return word_list


def main():
    input_file_path = 'emotions.txt'  # Update this with the path to your input file

    try:
        with open(input_file_path, 'r') as file:
            input_text = file.read()
            cleaned_text = clean_text(input_text)
            word_list = create_word_list(cleaned_text)

            # Convert all words to lowercase
            lowercase_word_list = [word.lower() for word in word_list]

            output_file_path = 'output.txt'
            with open(output_file_path, 'w') as output_file:
                for word in lowercase_word_list:
                    output_file.write(word + '\n')

            print(f"Cleaned and lowercase words saved to '{output_file_path}'.")
    except FileNotFoundError:
        print(f"File '{input_file_path}' not found.")


if __name__ == "__main__":
    main()
