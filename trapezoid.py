def Trapezoid_Area(base1,base2,height):
    
    calculation = .5 * (base1 + base2) * height

    return calculation

b1 = int(input("Enter length of the first base: "))
b2 = int(input("Enter length of the second base: "))
h = int(input("Enter length of the height: "))

result = Trapezoid_Area(b1,b2,h)
a = input("Do you want the measurements in feet? (y/n): ")
if a == "y":
    if result > 12:
        in_feet = int(result) / 12
        print(in_feet)
    else:
        print("Your result is less than 12 inches, so it won't be converted to feet.")
        print(result)
elif a == "n":
    print(result)