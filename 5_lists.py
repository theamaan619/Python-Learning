# Lists hold an ordered collection of items (mutable)

numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]

# Access items by index
print(numbers[0])        # 1
print(fruits[2])         # 'orange'

# Add an item to the end
fruits.append("grape")
print(fruits)

# Remove an item
fruits.remove("banana")
print(fruits)

# List slicing
print(numbers[1:4])      # [2, 3, 4]

# Length of list
print(len(fruits))
