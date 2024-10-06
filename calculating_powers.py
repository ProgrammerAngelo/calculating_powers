#make a method that calculate powers
def calculating_powers(base, exponent):

    if exponent == 0:
        return 1
    else:
        return base * calculating_powers(base, exponent - 1)
    
base = int(input("Enter a base number: "))
exponent = int(input("Enter a exponent: "))

result = calculating_powers(base, exponent)
print(f"The {base}^{exponent} is equal to {result}")

calculating_powers(base, exponent)