# We are making n stone piles! The first pile has n stones. 
# If n is even, then all piles have an even number of stones. 
# If n is odd, all piles have an odd number of stones. 
# Each pile must more stones than the previous pile but as few as possible. 
# Write a Python program to find the number of stones in each pile.
# Input: 2

stones = int(input("Enter number of piles: "))

piles = []

for i in range(stones):
    piles.append(stones)
    stones += 2

print("Stones in each pile:", piles)
