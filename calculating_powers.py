#make a method that calculate powers
def calculating_powers(base, exponent):
    # for base case
    if exponent == 0:
        return 1
    # for recursive case
    else:
        return base * calculating_powers(base, exponent - 1)

print("Hello user\n")

#for inputing base number
base = int(input("Please Enter base number: "))

#for inputing exponent
exponent = int(input("Please Enter exponent: "))

#for calculating the result
result = calculating_powers(base, exponent)
#for printing the result
print(f"The {base}^{exponent} is equal to {result}")

calculating_powers(base, exponent)