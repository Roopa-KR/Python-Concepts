#Lists in Python
#https://www.w3schools.com/python/python_lists.asp
#A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
#Example of a list
my_list = ["apple", "banana", "cherry"]
print(my_list)  # Output: ['apple', 'banana', 'cherry']
#Accessing list items
print(my_list[0])  # Output: 'apple'
print(my_list[1])  # Output: 'banana'
print(my_list[2])  # Output: 'cherry'
#Changing list items ,manipulating list items ,so lists are mutable
my_list[1] = "blueberry"
print(my_list)  # Output: ['apple', 'blueberry', 'cherry']
#Adding list items
my_list.append("orange")
print(my_list)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
my_list.insert(1, "grape")
print(my_list)  # Output: ['apple', 'grape', 'blueberry', 'cherry', 'orange']
#Removing list items
my_list.remove("blueberry")
print(my_list)  # Output: ['apple', 'grape', 'cherry', 'orange']
my_list.pop(1)
print(my_list)  # Output: ['apple', 'cherry', 'orange']
my_list.clear()
print(my_list)  # Output: []
#Adding list items using extend
my_list1 = ["apple", "banana", "cherry"]
my_list2 = ["orange", "grape", "melon"]
my_list1.extend(my_list2)
print(my_list1)  # Output: ['apple', 'banana', 'cherry', 'orange', 'grape', 'melon']
#Adding list items using + operator
my_list3 = my_list1 + my_list2
print(my_list3)  # Output: ['apple', 'banana', 'cherry', 'orange', 'grape', 'melon', 'orange', 'grape', 'melon']
