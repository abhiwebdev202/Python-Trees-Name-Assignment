# Python-Trees-Name-Assignment

In this report, I have discussed the python code that I wrote and the findings while executing this code. The python code using predetermined rules, creates three-letter abbreviations for a list of names and scores each abbreviation. The details regarding the key components, functions, and the expected output are given below:
Introduction:
The Python script's functions include reading a file with a list of names, producing three-letter abbreviations for each name according to predetermined guidelines, and scoring each abbreviation. The guidelines take into account the frequency and placement of letters in English words.
Code Components:
The main function in the code runs the whole code as an app which prompts two input fields to the users while executed. The first input field ask for file path for the input file, from which it reads the list of tree names. The second input field ask for file path for the output file, where the output of the python program that is the three-letter abbreviations for a list of names will be saved/written. The functions that are defined in the python code are:
read_ names(file_path): This function reads a file given as input from the file and outputs a list of names without removing tabs or spaces.
read_letter_ values(file_path): This function reads a file containing letter values and outputs a dictionary where the letters are the keys and the values are the associated integers. Here the letter is the key and corresponding integer value is the value for the key-value pair.
calculate_score(letter, position, is_first_letter, is_last_letter, letter_values): Determines a letter's score by looking at its frequency in English words as well as where it falls in the word. As per guidelines, if the letter is the first letter of the word then score is 0 and if it’s the last letter of the word then score is 5, if its E then the score is 20.
generate_abbreviations(name, letter_values): Using the given rules, this function creates three-letter abbreviations for a given name.
choose_best_abbreviation(abbreviations): Selects the abbreviation or abbreviations from a list of created abbreviations that have the lowest score.
These five functions are then used to define the main function which executes the code. I have used for loops and conditional statements accordingly in these functions as per assignment guidelines to obtain the necessary output.
main (): The primary function in charge of coordinating the script's execution. Input and output file paths are requested from the user, each name is processed, abbreviations are created, and the results are written to an output file.
Code Execution:
The user is prompted by the interactive script to enter the desired input file path, which contains a list of names and the output file path. In the script inside main () function, I also have provided the file path to the values file (values.txt) with letter frequencies, and this file must have the .txt extension.
The file paths that I used while executing the code are:
For values.txt:
C:\September Semester\Programming Languages for Data Science\Assignments\Python Assignment\values.txt
For Input:
C:\September Semester\Programming Languages for Data Science\Assignments\Python Assignment\trees.txt
For Output:
C:\September Semester\Programming Languages for Data Science\Assignments\Python Assignment\trees2.txt
Output of the Program:
To the designated output file, the script writes the original names (as they appear in the input file) together with their selected abbreviations and scores. When a name cannot be adequately shortened, a blank line is written. The abbreviations are listed on the same line, separated by spaces, if more than one has the same (best) score. Some sample outputs are:
Alder
ALD
Crab Apple
APP CRA
Common Ash
ASH COM
Silver Birch
BIR SIL
Downy Birch
BIR DOW
These are the first five outputs written in the output file named trees2.txt.




