def extract_integers_from_file(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove whitespace from both ends
            if not line:  # Skip empty lines
                continue
            parts = line.split()
            if len(parts) != 1:  # Skip lines with more than one integer
                continue
            try:
                number = int(parts[0])
                numbers.append(number)
            except ValueError:  # Ignore lines that cannot be parsed as an integer
                continue
    return numbers


def identify_duplicates(numbers):
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    duplicates = [number for number in frequency if frequency[number] > 1]
    return sorted(duplicates)


def save_duplicates_to_file(file_path, duplicates):
    with open(file_path, 'w') as file:
        for number in duplicates:
            file.write(f"{number}\n")


def handle_file(input_path, output_path):
    numbers = extract_integers_from_file(input_path)
    duplicates = identify_duplicates(numbers)
    save_duplicates_to_file(output_path, duplicates)


# Single file processing example
input_path = 'test_01.txt'
output_path = 'sample_results.txt'
handle_file(input_path, output_path)


# Loop for processing multiple files
input_paths = ['test_01.txt']  # Add more input file paths as needed
output_paths = ['sample_results.txt']  # Add corresponding output file paths

for input_path, output_path in zip(input_paths, output_paths):
    handle_file(input_path,output_path)
