# set comprehension is a concise way to create sets. It consists of curly braces containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in sets.
# Example of set comprehension
squared_set = {x**2 for x in range(10)}
print(squared_set)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
# Example of set comprehension with if condition
even_squared_set = {x**2 for x in range(10) if x % 2 == 0}
print(even_squared_set)  # Output: {0, 4, 16, 36, 64}
# Example of set comprehension with nested for loops    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_set = {num for row in matrix for num in row}
print(flattened_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Example of set comprehension with if-else condition
labels_set = {"Even" if x % 2 == 0 else "Odd" for x in range(10)}
print(labels_set)  # Output: {'Even', 'Odd'} (order may vary)
# Order may vary because sets are unordered collections
