# Number to letter relation
dict = {
    "2":["a","b","c"], 
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"]
}

# Special characters
special = {
    "a" : "(",
    "b" : ")",
    "c" : "-", 
    "d" : " "
}

# Function that converts strings to numbers as specified. 
def convert(number, dict, special):
    number = list(number.lower())
    for char in range(len(number)): 
        if number[char].isalpha():
            #Swap accordingly
            for i,j in dict.items():
                if number[char] in j :
                    number[char] = i  
        #Handle special characters            
        for i,j in special.items():
            if number[char] in j:
                number[char] = i                                       
    number = ''.join(number)   
    return number

# Function that prints given by "convert" 
def printnumber(number):
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
    return    
