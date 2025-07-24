# Generators yield values one at a time, saving memory

# A generator function that counts from 1 to n
def count_up_to(n):
    count = 1
    while count <= n:
        yield count     # 'yield' returns the current value and pauses the function
        count += 1      # Next time the generator is called, it resumes from here

# Call the generator function — this doesn't run it yet
# It returns a generator object that we can loop over
counter = count_up_to(5)

# Loop through the generator
# Each time through the loop, 'yield' gives the next value
for num in counter:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5
