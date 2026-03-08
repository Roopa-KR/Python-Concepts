#Data types in python
#Data types are the classification of data that tells the compiler or interpreter how the programmer intends to use the data. In Python, there are several built-in data types that you can use to store and manipulate data. Some of the most common data types in Python include:
# 1. Integer (int): Whole numbers without a decimal point.
# 2. Float (float): Numbers with a decimal point.
# 3. String (str): A sequence of characters enclosed in quotes.
# 4. Boolean (bool): A data type that can only have one of two values: True or False.
# 5. List (list): An ordered collection of items that can be of different data types.
# 6. Tuple (tuple): An ordered, immutable collection of items that can be of different data types.
# 7. Dictionary (dict): A collection of key-value pairs where each key is unique.
# 8. Set (set): An unordered collection of unique items.
# You can use the built-in type() function to check the data type of a variable. For example:
x = 10
print(type(x))  # Output: <class 'int'>
y = 3.14
print(type(y))  # Output: <class 'float'>
name = "Alice"
print(type(name))  # Output: <class 'str'>
is_valid = True
print(type(is_valid))  # Output: <class 'bool'>
my_list = [1, 2, 3, "hello"]
print(type(my_list))  # Output: <class 'list'>
my_tuple = (1, 2, 3, "world")
print(type(my_tuple))  # Output: <class 'tuple'>
my_dict = {"name": "Alice", "age": 30}
print(type(my_dict))  # Output: <class 'dict'>
my_set = {1, 2, 3, 4}
print(type(my_set))  # Output: <class 'set'>
