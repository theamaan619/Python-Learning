# Strings are sequences of characters

greeting = "Hello"
name = "Amaan"

# Concatenation
message = greeting + " " + name
print(message)

# Length of the string
print("Length:", len(message))

# Access specific character (indexing starts from 0)
print("First character:", message[0])

# Slicing
print("Substring:", message[1:5])  # 'ello'

# String methods
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Replace:", message.replace("Amaan", "Ahmed"))
