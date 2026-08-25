x=float(input("Enter distance in kilometers: "))
y=0.621371
z=x*y
print("Distance in miles:",z)

a=input("Do you want to convert another distance? (yes/no): ")
if a=="yes":
    q=float(input("Enter distance in kilometers: "))
    r=q*y
    print("Distance in miles:",r)
else:
    print("Program ended.")
