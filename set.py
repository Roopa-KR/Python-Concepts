#sets in python
# sets are unordered collection of unique items
# sets are mutable, but the items in the set must be immutable
# sets are defined using curly braces {} or the set() function
# creating a empty set
my_set = set()
print(my_set)  # Output: set()
# creating a set with some elements
my_set = {1, 2, 3, 4, 5}
#printing the set
print(my_set)  # Output: {1, 2, 3, 4, 5}
# adding an element to the set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
# adding a duplicate element to the set
my_set.add(3)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6} (no change, as sets do not allow duplicates)
# removing an element from the set
my_set.remove(4)
print(my_set)  # Output: {1, 2, 3, 5, 6}
# checking if an element is in the set
print(3 in my_set)  # Output: True
print(4 in my_set)  # Output: False
# set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# union of sets
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5}
# intersection of sets
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3}  
# difference of sets
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}
# symmetric difference of sets
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
