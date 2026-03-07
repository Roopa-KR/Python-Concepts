#keywords in python
#keywords are reserved words in python which have special meaning and cannot be used as variable names, function names, or any other identifiers.
# Some examples of keywords in Python include:
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# You can get a list of all the keywords in Python by using the keyword module:
import keyword
print(keyword.kwlist)
# In the example above, we import the keyword module and then print the list of keywords using keyword.kwlist. This will display all the reserved keywords in Python that you should avoid using as identifiers in your code.
#The keywords in Python are case-sensitive, which means that they must be written in lowercase. For example, "if" is a keyword, but "If" or "IF" are not recognized as keywords and can be used as variable names (although it is not recommended to use them as such).
# It is important to remember that keywords cannot be used as variable names, function names, or any other identifiers in your code. If you try to use a keyword as an identifier, you will get a syntax error. For example:
#If x==5:
# This will cause a syntax error because "if" is a keyword
