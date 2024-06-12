def read_integers_from_file(test_01.txt.res):
    integers = []
    with open(test_01.txt.res, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 1:
                continue
            try:
                number = int(parts[0])
                integers.append(number)
            except ValueError:
                continue
    return integers

def find_duplicates(integers):
    count_dict = {}
    for num in integers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    duplicates = [num for num, count in count_dict.items() if count > 1]
    return sorted(duplicates)

def write_duplicates_to_file(duplicates, file_path):
    with open(file_path, 'w') as file:
        for num in duplicates:
            file.write(f"{num}\n")

def process_input_file(input_file, output_file):
    integers = read_integers_from_file(input_file)
    duplicates = find_duplicates(integers)
    write_duplicates_to_file(duplicates, output_file)

# Example usage
input_file = 'sample_data.txt'
output_file = 'sample_results.txt'
process_input_file(input_file, output_file)