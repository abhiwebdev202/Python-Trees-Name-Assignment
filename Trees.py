# Reading Tree names from a text file
def read_names(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


# Reading letter values from a text file
def read_letter_values(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return {line.split()[0]: int(line.split()[1]) for line in lines}


# Caculating letter score
def calculate_score(letter, position, is_first_letter, is_last_letter, letter_values):
    if is_first_letter:
        return 0
    elif is_last_letter:
        return 20 if letter == 'E' else 5
    else:
        position_value = 1 if position == 2 else 2 if position == 3 else 3
        return position_value + letter_values.get(letter, 0)


#Creating Three letter abbreviations

def generate_abbreviations(name, letter_values):
    words = [word.strip("'") for word in name.split() if word.isalpha()]
    abbreviations = set()

    for word in words:
        for i in range(len(word) - 2):
            abbreviation = word[0] + word[i + 1] + word[i + 2]
            score = calculate_score(abbreviation[1], i + 2, i == 0, i == len(word) - 3, letter_values)
            abbreviations.add((abbreviation, score))

    return abbreviations


# Choosing the abbreviations
def choose_best_abbreviation(abbreviations):
    if not abbreviations:
        return None

    min_score = min(abbreviations, key=lambda x: x[1])[1]
    return [abbr for abbr, score in abbreviations if score == min_score]


# The main function to run the whole script
def main():
    input_file_path = input("Enter the input file path: ")
    output_file_path = input("Enter the output file path: ")

    names = read_names(input_file_path)
    letter_values = read_letter_values(r'C:\September Semester\Programming Languages for Data Science\Assignments\Python Assignment\values.txt')

    with open(output_file_path, 'w') as output_file:
        for name in names:
            output_file.write(name + '\n')
            abbreviations = generate_abbreviations(name.upper(), letter_values)

            selected_abbreviations = choose_best_abbreviation(abbreviations)
            if selected_abbreviations:
                output_file.write(' '.join(selected_abbreviations) + '\n')
            else:
                output_file.write('\n')


if __name__ == "__main__":
    main()