# Write a Python program that accepts the user's first and last name
# and prints them in reverse order with a space between them.

first_name = input("First name: ")
last_name = input("Last name: ")

names = [first_name, last_name]

print(" ".join(reversed(names)))
print(type(names))