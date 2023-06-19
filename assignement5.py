#!/usr/bin/env python
# coding: utf-8
1.)What does an empty dictionary's code look like?
    In Python, an empty dictionary is represented by a pair of curly braces with no key-value pairs inside. 
    The code for an empty dictionary would simply be:
    {}
    assigning the values of empty dictonary
    my_dict = {}2. What is the value of a dictionary value with the key 'foo' and the value 42?
    he value of a dictionary with the key 'foo' and the value 42 can be accessed using the key within square brackets.
    Here's an example:
    
# In[1]:


my_dict = {'foo': 42}
value = my_dict['foo']
print(value)

3. What is the most significant distinction between a dictionary and a list? 
  Structure:
    A dictionary is an unordered collection of key-value pairs enclosed in curly braces {}. 
    Each key in a dictionary must beunique, and it is associated with a value.
    A list, on the other hand, is an ordered collection of items enclosed in square brackets []. 
    The items in a list are ordered and can be accessed by their index.
    
 Data Organization:
     Dictionaries use keys to organize and access data. Each key is unique and acts as an identifier for its associated value. 
     This allows for efficient lookup and retrieval of values based on the key.
     Lists organize data based on their position or index. Each item in a list has an index value, starting from 0 for the
     first item. 
     This allows for accessing items by their index position.
     
 Data Retrieval:

In a dictionary, values are accessed by providing the corresponding key. 
The key is used as a lookup mechanism to retrieve the associated value. 
Dictionaries provide fast access to values based on keys, but the order of retrieval is not guaranteed.
In a list, values are accessed by their index. You can retrieve an item from a list by specifying its index position. Lists provide efficient access to items based on their position in the list, 
but searching for a specific item requires iterating through the list.

Mutability:
Both dictionaries and lists are mutable, meaning their elements can be modified. You can add, remove, or modify items in both data structures.
    4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
    f you try to access spam['foo'] and spam is {'bar': 100}, you will encounter a KeyError.
    This error occurs because the dictionary spam does not have a key named 'foo'. 
    When you try to access a key that doesn't exist in a dictionary using the square bracket notation, a KeyError is raised.
5.) If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
       In the context of a dictionary stored in spam, there is no practical difference between the expressions 'cat' in spam 
       and 'cat' in spam.keys(). Both expressions are used to check if the key 'cat' exists in the dictionary spam.

    Here's a breakdown of each expression:

      1.)'cat' in spam: This expression checks if the key 'cat' exists in the dictionary spam.
        It returns True if the key exists, and False otherwise.

      2.)'cat' in spam.keys(): This expression retrieves the keys of the spam dictionary using the keys() method and then checks 
        if 'cat' is present among those keys.It also returns True if the key exists, and False otherwise.

Both expressions essentially achieve the same result of checking for the existence of the key 'cat' in the dictionary. However, the second expression explicitly uses the keys() method to retrieve the keys, which may be slightly less efficient than the first expression since it involves an additional method call.

Therefore, it is generally more common and preferable to use 'cat' in spam to check for the presence of a key in a dictionary.6.) If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
    n the context of a dictionary stored in spam, the expressions 'cat' in spam and 'cat' in spam.values() have different purposes and yield different results.

    'cat' in spam: This expression checks if the key 'cat' exists in the dictionary spam.
    It returns True if the key exists, and False otherwise. It is used to determine if 'cat' is a key in the dictionary.

    'cat' in spam.values(): This expression checks if the value 'cat' exists in any of the values in the dictionary spam.
    It returns True if the value exists in any of the dictionary's values, and False otherwise. 
    It is used to determine if 'cat' is a value in the dictionary.


# In[9]:


spam = {'name': 'Alice', 'age': 25, 'pet': 'cat'}

print('name' in spam)           # True
print('cat' in spam)            # False
print('cat' in spam.values())   # True
print('Alice' in spam.values()) # False

n the example above, 'name' in spam returns True because 'name' is a key in the dictionary. 'cat' in spam returns False because 'cat' is not a key in the dictionary. However, 'cat' in spam.values() returns True because 'cat' is present as a value in the dictionary (associated with the key 'pet').

To summarize, 'cat' in spam checks for the existence of the key 'cat' in the dictionary, while 'cat' in spam.values() checks for the existence of the value 'cat' in any of the dictionary's values.







7. What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'




# In[15]:


if 'color' not in spam:
    spam['color'] = 'black'
    #shotcut of writing this code
    spam.setdefault('color', 'black')

8. How do you "pretty print" dictionary values using which module and function?
    To "pretty print" dictionary values in Python, you can use the pprint module and its pprint function.
    The pprint module provides a way to format and display complex data structures,
    such as dictionaries, in a more readable and visually appealing format.

    Here's an example of how to use pprint to pretty print a dictionary:
    
# In[11]:


import pprint

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

pprint.pprint(my_dict)


import pprint

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

pprint.pprint(my_dict)

Both pprint.pprint() and pprint() from the pprint module can be used to achieve pretty printing of dictionary values.