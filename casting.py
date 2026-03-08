#Type casting is the process of converting a variable from one type to another. In Python, you can use built-in functions to perform type casting. Here are some common type casting functions:
# 1. int(): Converts a value to an integer. For example:
x = 3.14
y = int(x)      
print(y)  # Output: 3
# 2. float(): Converts a value to a float. For example:
a = 10
b = float(a)
print(b)  # Output: 10.0
# 3. str(): Converts a value to a string. For example:
num = 42
text = str(num)
print(text)  # Output: "42"
# 4. bool(): Converts a value to a boolean. For example:
value = 0
is_true = bool(value)
print(is_true)  # Output: False
# You can also use type casting to convert between different data types. For example:
num_str = "123"
num_int = int(num_str)
print(num_int)  # Output: 123
#types of type casting
# 1. Implicit Type Casting: This is when Python automatically converts one data type to another without the programmer's intervention. For example:
x = 5       # int
y = 3.14    # float
result = x + y  # Implicitly converts x to float
print(result)  # Output: 8.14
# 2. Explicit Type Casting: This is when the programmer explicitly converts one data type to another using type casting functions. For example:
num_str = "456"
num_int = int(num_str)  # Explicitly converts num_str to int
print(num_int)  # Output: 456

