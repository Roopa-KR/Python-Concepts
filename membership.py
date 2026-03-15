# Membership Operators in Python
# in and not in
# in operator checks if a value is present in a sequence (like a list, tuple, string, etc.)
# not in operator checks if a value is not present in a sequence
# Example with a list
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False
print(3 not in my_list)  # Output: False
print(6 not in my_list)  # Output: True
# Example with a string
my_string = "Hello, World!"
print("Hello" in my_string)  # Output: True
print("Python" in my_string)  # Output: False
print("Hello" not in my_string)  # Output: False
print("Python" not in my_string)  # Output: True
# Example with a tuple
my_tuple = (1, 2, 3, 4, 5)
print(3 in my_tuple)  # Output: True
print(6 in my_tuple)  # Output: False
print(3 not in my_tuple)  # Output: False
print(6 not in my_tuple)  # Output: True
# Example with a set
my_set = {1, 2, 3, 4, 5}    
print(3 in my_set)  # Output: True
print(6 in my_set)  # Output: False
print(3 not in my_set)  # Output: False
print(6 not in my_set)  # Output: True  
