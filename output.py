# Print Text
# You have already learned that you can use the print() function to display text or output values:
print("Hello, World!")
# The text you want to display must be enclosed in quotation marks (either single or double quotes).
# You can also print numbers:
print(42)
# You can print the result of a calculation:
print(2 + 3)
# You can print multiple items by separating them with commas:
print("The answer is", 42)
# The print() function can take multiple arguments, and it will display them separated by a space by default.
print("The sum of 2 and 3 is", 2 + 3)

# You can also use the end parameter to specify what to print at the end of the output. By default, it is a newline character (\n), which means that each print statement will start on a new line:
print("Hello", end=" ")
print("World!")
# In the example above, the end parameter is set to a space (" "), so the output will be "Hello World!" on the same line.
#try to change the end parameter to something else, like a comma or a dash, to see how it affects the output:
print("Hello", end=", ")
print("World!")
print("Hello", end="-")
print("World!")