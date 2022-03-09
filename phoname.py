from phonamef import convert,printnumber,dict,special

# Get string 
print("Ingresa un número de teléfono:  ")
number = str(input())

#Convert number to be printed 
number = convert(number,dict,special)

printnumber(number)


    





