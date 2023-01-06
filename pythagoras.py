def Pythagoras(base1,base2):
    
    c_squared = int(base1**2) + int(base2**2)
    c = c_squared**(1/2)

    return c

first_leg = int(input("Input the length of the first leg: "))
second_leg = int(input("Input the length of the other leg: "))

result = Pythagoras(first_leg, second_leg)

print("Your result is: ",result)
