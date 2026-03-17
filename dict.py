#Dictionary in python
#Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)  
#Accessing values in a dictionary
print(my_dict["name"])  # Output: John
print(my_dict.get("age"))  # Output: 30
#Adding or updating key-value pairs in a dictionary
my_dict["email"] = "john@example.com"
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com'}      
#Printng all keys in a dictionary
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city', 'email'])
#Printing all values in a dictionary    
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York']
#adding a new key-value pair to the dictionary
my_dict["country"] = "USA"
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com', 'country': 'USA'}
#Updating an existing key-value pair in the dictionary
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com', 'country': 'USA'}    

