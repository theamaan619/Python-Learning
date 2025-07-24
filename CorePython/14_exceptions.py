# Exceptions are used to handle errors gracefully

try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("That's not a valid number!")
finally:
    print("End of program.")
