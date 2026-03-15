#Logical operators are used to combine conditional statements.
#Logical operators include:
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
# # Logical AND
x = 5
print(x > 3 and x < 10)  # Output: True 
print(x > 3 and x < 5)   # Output: False
# Logical OR
y = 8
print(y < 5 or y < 10)  # Output: True
print(y < 5 or y < 8)   # Output: False
# Logical NOT
z = 12
print(not(z > 10))  # Output: False
print(not(z < 10))  # Output: True
