# Write a Python program that accepts a list of integers 
# and calculates the length and the fifth element.
# Return true if the length of the list is 8 and 
# the fifth element occurs thrice in the said list.
# Input:
# [19, 19, 15, 5, 5, 5, 1, 2]


numbers = [19, 19, 15, 5, 5, 5, 1, 2]

result = len(numbers) == 8 and numbers.count(numbers[4]) == 3

print(result)