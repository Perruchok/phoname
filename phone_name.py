from helpers import convert, print_number

# Get string 
print("Ingresa un número de teléfono:  ")
unconverted_number = str(input())

# Convert number to be printed 
converted_number = convert(unconverted_number)

# Print numbers:
print_number(converted_number)
