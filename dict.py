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
#adding two new key-value pairs to the dictionary using the update() method
my_dict.update({"phone": "123-456-7890", "occupation": "Software Engineer"})
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com', 'country': 'USA', 'phone': '123-456-7890', 'occupation': 'Software Engineer'}    
#Removing a key-value pair from the dictionary using the del statement
del my_dict["email"]
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA', 'phone': '123-456-7890', 'occupation': 'Software Engineer'}
#Removing a key-value pair from the dictionary using the pop() method
removed_value = my_dict.pop("phone")    
print(removed_value)  # Output: 123-456-7890
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA', 'occupation': 'Software Engineer'}
#Iterating through a dictionary
for key in my_dict:
    print(key)  # Output: name, age, city, country, occupation (order may vary) 
for value in my_dict.values():
    print(value)  # Output: John, 31, New York, USA, Software Engineer (order may vary)
for key, value in my_dict.items():
    print(f"{key}: {value}")  # Output: name: John, age: 31, city: New York, country: USA, occupation: Software Engineer (order may vary)
#Checking if a key exists in the dictionary
print("name" in my_dict)  # Output: True
#Checking if a value exists in the dictionary
print("John" in my_dict.values())  # Output: True
#list in dictionary
my_dict["hobbies"] = ["reading", "traveling", "coding"]     
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA', 'occupation': 'Software Engineer', 'hobbies': ['reading', 'traveling', 'coding']}
#duplicate keys in a dictionary
my_dict = {"name": "John", "age": 30, "name": "Jane"}
print(my_dict)  # Output: {'name': 'Jane', 'age': 30} (the value of the duplicate key "name" is overwritten by the last occurrence)

