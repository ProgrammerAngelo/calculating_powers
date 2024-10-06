#make a method that calculate powers
def calculating_powers(base, exponent):

    if exponent == 0:
        return 1
    else:
        return base * calculating_powers(base, exponent - 1)
    
base = float(input("Enter a base number: "))
exponent = float(input("Enter a exponent: "))

calculating_powers()
#add a recursive case