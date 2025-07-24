# Lambda creates anonymous functions

add = lambda a, b: a + b
print("Lambda sum:", add(2, 3))

# map applies a function to all items in a list
nums = [1, 2, 3]
doubles = list(map(lambda x: x * 2, nums))
print(doubles)

# filter filters items based on a condition
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
