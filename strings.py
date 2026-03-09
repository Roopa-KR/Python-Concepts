#strings in python
#string is a sequence of characters

#creating a string
name = "John"
#string concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: "John Doe"
#string formatting
age = 30
greeting = f"My name is {name} and I am {age} years old."
print(greeting)  # Output: "My name is John and I am 30 years old."
#string methods
text = "Hello, World!"
print(text.upper())  # Output: "HELLO, WORLD!"
print(text.lower())  # Output: "hello, world!"
print(text.split(", "))  # Output: ["Hello", "World!"]
print(text.replace("World", "Python"))  # Output: "Hello, Python!"
