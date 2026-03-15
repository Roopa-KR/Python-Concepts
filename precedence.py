#Operator precedence
#https://www.tutorialspoint.com/python/python_operators_precedence.htm
#Operator precedence determines the order in which operators are evaluated in an expression.
#In Python, the operator precedence is as follows (from highest to lowest):
#1. Parentheses ( )
#2. Exponentiation ( ** )
#3. Unary plus and minus ( +x, -x )
#4. Multiplication, division, floor division, and modulus ( *, /, //, % )
#5. Addition and subtraction ( +, - )
#6. Bitwise shift operators ( <<, >> )
#7. Bitwise AND ( & )
#8. Bitwise XOR ( ^ )
#9. Bitwise OR ( | )
#10. Comparison operators ( ==, !=, >, <, >=, <= )
#11. Identity operators ( is, is not )
#12. Membership operators ( in, not in )
#13. Logical operators ( and, or, not )
#14. Assignment operators ( =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>=, <<= )
#15. Conditional expression ( if ... else )
#16. Lambda expression ( lambda )
#Example of operator precedence
result = 3 + 4 * 2 / (1 - 5) ** 2
print(result)  # Output: 3.5