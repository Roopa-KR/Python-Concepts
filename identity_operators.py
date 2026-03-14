#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object with the same memory location.
#Identity operators include:
#is (returns True if both variables are the same object)
#is not (returns True if both variables are not the same object)
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)  # Output: False
print(x is z)  # Output: True
print(x is not y)  # Output: True