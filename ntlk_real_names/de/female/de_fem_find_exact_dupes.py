def remove_exact_duplicates(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()

    unique_lines = []
    seen_lines = set()

    for line in lines:
        if line not in seen_lines:
            unique_lines.append(line)
            seen_lines.add(line)

    with open(output_filename, 'w') as output_file:
        output_file.writelines(unique_lines)

if __name__ == "__main__":
    input_filename = "de_fem_hyph.txt"
    output_filename = "output_no_duplicates.txt"

    remove_exact_duplicates(input_filename, output_filename)
    print(f"Exact duplicate lines removed. Result saved to {output_filename}")