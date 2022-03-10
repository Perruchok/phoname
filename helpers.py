from typing import List

number_matrix = {
    ("0",): "0",  # TODO: add this file inside of the symbols folder.
    ("1",): "1",
    ("2", "a", "b", "c"): "2",
    ("3", "d", "e", "f"): "3",
    ("4", "g", "h", "i"): "4",
    ("5", "j", "k", "l"): "5",
    ("6", "m", "n", "o"): "6",
    ("7", "p", "q", "r","s"): "7",
    ("8", "t", "u", "v"): "8",
    ("9", "w", "x", "y", "z"): "9",
}

symbol_to_file = {
    "(": "open-parenthesis.txt",
    ")": "close-parenthesis.txt",
    "+": "plus.txt",
    "-": "dash.txt",
    " ": "space.txt",
}
for possible_letters, number in number_matrix.items():
    for possible_letter in possible_letters:
        symbol_to_file[possible_letter] = f"{number}.txt"



def convert(unclean_phone_number: str) -> List[str]:
    """
        Function that converts strings to numbers as specified.
    """

    clearn_phone_number = list()
    for char in unclean_phone_number.lower():
        # Add character.
        clearn_phone_number.append(
            symbol_to_file[char]
        )

        # Add Space.
        clearn_phone_number.append("space.txt")

    return clearn_phone_number


def _print_number(line_to_print):
    print(line_to_print)


def print_number(number_files):
    """
        Function that prints given by 'convert'.
    """

    # Map all the files in a dict:
    file_to_character_list = dict()
    for number_file in number_files:
        try:
            file_obj = open(f"symbols/{number_file}", "r")

        except FileNotFoundError:
            raise FileNotFoundError(
                f"symbols/{number_file} file was not found."
            )

        file_to_character_list[number_file] = file_obj.readlines()

        file_obj.close()

    # Each file has eight rows.
    number_of_row = 8
    line_to_print = ""
    for row in range(number_of_row):
        for number_file in number_files:
            number_file_lines = file_to_character_list[number_file]

            #There must be a "\n" as the last char of the string, so remove it.
            line_to_print += number_file_lines[row].replace("\n", "")

        line_to_print += "\n"

    _print_number(line_to_print)
