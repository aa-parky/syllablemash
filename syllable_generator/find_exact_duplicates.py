from collections import Counter


def find_exact_duplicate_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    line_counter = Counter(lines)
    duplicate_line_numbers = {line: [i + 1 for i, l in enumerate(lines) if l == line] for line, count in
                              line_counter.items() if count > 1}

    return duplicate_line_numbers


def write_results_to_file(results, output_filename):
    with open(output_filename, 'w') as file:
        if results:
            for line, line_numbers in results.items():
                file.write(f"Line: {line.strip()} | Line Numbers: {', '.join(map(str, line_numbers))}\n")
        else:
            file.write("No exact duplicate lines found.\n")


if __name__ == "__main__":
    input_filename = "output.txt"
    output_filename = "find_exact_duplicates.txt"

    duplicate_line_numbers = find_exact_duplicate_lines(input_filename)

    if duplicate_line_numbers:
        print("Exact duplicate lines found:")
        for line, line_numbers in duplicate_line_numbers.items():
            print(f"Line: {line.strip()} | Line Numbers: {', '.join(map(str, line_numbers))}")
    else:
        print("No exact duplicate lines found.")

    write_results_to_file(duplicate_line_numbers, output_filename)
    print(f"Results written to {output_filename}")
