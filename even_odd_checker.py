# Write a Python program that determines whether a given number 
# (accepted from the user) is even or odd, 
# and prints an appropriate message to the user.

while True:
        number = int(input("Enter a number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

        