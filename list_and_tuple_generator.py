# Write a Python program that accepts a sequence of 
# comma-separated numbers from the user and 
# generates a list and a tuple of those numbers.

numbers = input("Enter numbers: ")

numbers_list = numbers.split()
numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)
