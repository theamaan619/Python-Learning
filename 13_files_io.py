# File Input/Output

# Write text to a file
with open("example.txt", "w") as file:
    file.write("Hello, file!\n")

# Read text from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:", content)
