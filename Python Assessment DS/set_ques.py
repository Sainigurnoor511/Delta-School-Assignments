# Create a set of prime numbers less than 10.

set1 = {x for x in range(1, 10) if x > 1 and all(x % i != 0 for i in range(2, x))}
print(set1)

# Write a program to find the common elements between two sets.

set2 = {3, 5, 7, 11, 13}
common_elements = set1.intersection(set2)
print(common_elements)