symbol_relations = {
    "1.txt": "1",
    "2.txt": ["2", "a", "b", "c"], 
    "3.txt": ["3", "d", "e", "f"],
    "4.txt": ["4", "g", "h", "i"],
    "5.txt": ["5", "j", "k", "l"],
    "6.txt": ["6", "m", "n", "o"],
    "7.txt": ["7", "p", "q", "r", "s"],
    "8.txt": ["8", "t", "u", "v"],
    "9.txt": ["9", "w", "x","y", "z"],
    "open_parenthesis.txt": "(",
    "close_parenthesis.txt": ")",
    "minus.txt": "-", 
    "space.txt": " ",
    "+.txt": "+",
}


symbol_to_file = {}
for file_name, posible_letters in symbol_relations.items():
    for posible_letter in posible_letters:
        symbol_to_file[posible_letter] = file_name


def convert(unconverted_number): 
    """
        Function that converts strings to numbers as specified. 
    """

    #Do conversion
    converted_number_file_list = list()
    for char in unconverted_number: 
        
        converted_number_file_list.append(
            symbol_to_file[char.lower()]
            )   

        #Ad space to solve line error
        converted_number_file_list.append("space.txt")     
 
    return converted_number_file_list


def print_number(converted_number_file_list):
    """
        Function that prints number given by "convert" 
    """

    # Save required system files into buffer 
    file_buffer = dict()
    for file in converted_number_file_list:
        try: 
             file_obj = open(f"characters/{file}")

        except FileNotFoundError: 
            raise FileNotFoundError(
                f"Character {file} is not valid."
            )

        file_buffer[file] = file_obj.readlines()

        file_obj.close()

    # Print to terminal
    file_lines = 8 

    line_to_print = ""
    for line in range(file_lines): 
        for file in converted_number_file_list:

            character_file_lines = file_buffer[file]

            #There must be a \n at the end of the line, so remove it
            line_to_print += character_file_lines[line].replace("\n", "")

        line_to_print += "\n"

    return line_to_print