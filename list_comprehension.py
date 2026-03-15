#List comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
#Example of list comprehension
squares = [x**2 for x in range(10)] 
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#Example of list comprehension with if condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]
#Example of list comprehension with nested for loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9] 
#Example of list comprehension with if-else condition
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print(labels)  # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']    

