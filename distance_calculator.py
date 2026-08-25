#This asks for the user's input.
km = float(input("Enter distance in kilometers: "))
#cf here means conversion factor.
cf = 0.621371
#mi is shortened form of miles.
mi = km * cf

print("Distance in miles:", mi)
#This part asks the user if they want to continue running the code using an if-else structure
q = input("Do you want to convert another distance? (yes/no): ")

if q == "yes":
#This part repeats the code from the start.
    q = float(input("Enter distance in kilometers: "))
    km2 = q * cf
    print("Distance in miles:", km2)
else:
    print("Program ended.")
