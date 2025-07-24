# Sets are unordered collections of unique items

my_set = {1, 2, 3, 2, 1}
print(my_set)   # Output: {1, 2, 3}

# Add an element
my_set.add(4)
print(my_set)

# Remove an element
my_set.remove(2)
print(my_set)

# Set operations
another_set = {3, 4, 5}
print("Union:", my_set | another_set)
print("Intersection:", my_set & another_set)
