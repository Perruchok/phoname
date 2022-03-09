# Get string 
print("Ingresa un número:  ")
number = str(input())

#Convert string to number as specified.

# Print number 
for n in range(8): # File texts have only 8 lines
    linetoprint = ""
    # Built the nth line:
    for i in number:
        try:
            f = open(f'{i}.txt', 'r')
        except FileNotFoundError:
            print("Entrada no válida")
            exit()
        lines = f.readlines()
        linetoprint = linetoprint + lines[n][:-1] #There must be a "/n" as the last char of the string, so remove it. 
        f.close()
    print(linetoprint)
    





