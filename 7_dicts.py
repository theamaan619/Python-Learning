# Dictionaries store data as key-value pairs

student = {
    "name": "Amaan",
    "age": 25,
    "is_student": True
}

# Access values using keys
print(student["name"])

# Add a new key-value pair
student["grade"] = "A"
print(student)

# Remove a key-value pair
del student["age"]
print(student)

# Get all keys
print(student.keys())
