# For loop - repeat actions a certain number of times

for i in range(5):
    print("Iteration", i)

# While loop - repeat actions while a condition is true
count = 0
while count < 3:
    print("Counting:", count)
    count += 1

# break and continue
for i in range(5):
    if i == 3:
        break   # Stop loop if i is 3
    if i == 1:
        continue # Skip this iteration if i is 1
    print(i)
