
# cf here means conversion factor.
cf = 0.621371

while True:
    # This asks for the user's input.
    km = float(input("Enter distance in kilometers: "))

    # mi is the shortened form of miles.
    mi = km * cf

    print("Distance in miles:", mi)

    # .strip() removes extra spaces, while .lower() converts the input to lowercase.
    q = input("Do you want to convert another distance? (yes/no): ").strip().lower()

    if q == "no":
        print("Program ended.")
        break
    elif q == "yes":
        continue
    else:
        print("Invalid choice. The program will end.")
        break
