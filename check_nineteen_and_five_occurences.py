# Write a Python program to find a list of integers with 
# exactly two occurrences of nineteen and at least three occurrences of five. 
# Return True otherwise False.
# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]


numbers = [19, 19, 15, 5, 3, 5, 5, 2]

result = numbers.count(19) == 2 and numbers.count(5) >= 3

print(result)
