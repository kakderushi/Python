#!/usr/bin/env python
# coding: utf-8
1.) What exactly is []?
   Ans:An empty brackets[] typically denoate list or array.2.) In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
# In[1]:


spam=[2,4,6,8,10]
spam
spam[3]='hello'
spam

Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
3.) What is the value of spam[int(int('3' * 2) / 11)]?

# In[2]:


spam=[int(int(3*2)/11)]

spam

4.) What is the value of spam[-1]?
# In[3]:


spam=['a','b','c','d']
print(spam[-1])

5.) What is the value of spam[:2]?

# In[4]:


spam[:2]

Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
6. What is the value of bacon.index('cat')?
7. How does bacon.append(99) change the look of the list value in bacon?
8. How does bacon.remove('cat') change the look of the list in bacon?
# In[5]:


#6. What is the value of bacon.index('cat')?
bacon=[3.14,'cat',11,'cat',True]
print(bacon.index('cat'))


# In[6]:


#7. How does bacon.append(99) change the look of the list value in bacon?
bacon=[3.14,'cat',11,'cat',True]
print(bacon.append(99))
bacon

append() function in list is add the values at the last of the list
that's result we would see in the above code.
# In[7]:


#8. How does bacon.remove('cat') change the look of the list in bacon?
bacon=[3.14,'cat',11,'cat',True]
bacon.remove('cat')
bacon

bacon.remove('cat') can remove the item from the list
which is present in the bacon.remove('cat').9. What are the list concatenation and list replication operators?

    (i)List concatenation operator ('+'):The list concatenation operator is used to concatenate two
    or more lists,resulting in a new list that contains all the elements from the operands.
# In[8]:


list1=[1,2,3,4]
list2=[5,6,7,8]
result=list1+list2
result

    (ii)List replication operator('*'):The lsit replication operator is used to replicate a list
        by a specified number.It creates a new list that contains multiple copies of the orignal values.
# In[9]:


orignal_list=[1,3,4,]
replicated_list=orignal_list*3
replicated_list

10. What is difference between the list methods append() and insert()?
    
    append(): This method is used to add an element to the end of a list. It takes a single argument, 
    which is the element to be added, and appends it to the end of the list.

# In[10]:


list1=[1,2,3,4]
list1.append(99)
list1

here we add 99 at the end of the list using append() methodinsert(): This method is used to insert an element at a specific index in a list.
It takes two arguments: the index at which to insert the element, 
and the element to be inserted.
# In[11]:


my_list=[1,3,4,5]
my_list.insert(1,6)
my_list

11. What are the two methods for removing items from a list?
    (i)remove(): This method is used to remove the first occurrence of a specific value from the list. 
    It takes a single argument, which is the value to be removed.
# In[12]:


my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list) 

 (ii)pop(): This method is used to remove an element from a specific index in the list and return its value. 
 It takes an optional argument, which is the index of the element to be removed. If no index is specified, 
 it removes and returns the last element in the list.
# In[13]:


my_list = [1, 2, 3]
removed_element = my_list.pop(1)
print(removed_element) 
print(my_list) 

12. Describe how list values and string values are identical.
   1) Sequence of Elements: Both lists and strings are sequences of elements. 
    In a list, the elements can be of any data type (e.g., numbers, strings, objects), while in a string, 
    the elements are characters.

    2)Indexing: Both lists and strings allow access to individual elements by their index. 
    Elements in both lists and strings are ordered and can be accessed using positive and negative indices.

    3)Slicing: Both lists and strings support slicing operations. 
    Slicing allows you to extract a portion of the sequence by specifying a range of indices.

    4)Iteration: You can iterate over both lists and strings using loops. 
    This allows you to access each element in the sequence one by one.13. What's the difference between tuples and lists?
    Difference between list and tuple:
    Mutability:tuples are immutable, meaning their element cannot be changed once tuple is created.
    In contrast, lists are mutable. allowing to addition, removal and modification of element.
    
    Syntax:tuples are identified using parenthesis () (1,3,4).while
    lists are defined using square brackets [] [2,4,5].
    
    Usage:Tuples are usually represent collections of related ,immutable data, where the order
    of element is important .they are commonly used in co-ordinates,data base records or multiple
    values from the function. lists on the hand more versatile and commonly used for dynamic collections
    of element that may change or need modification over the time.
    
    Operations:lists are provide a wide range of built-in-methods for modifying,sorting and
    manipulating the list.such as (insert(),remove(),sort() etc).
    tuples are immutable ,so it have limited set of methods, mainly they provide accessing elements and 
    performing basic operations like(index(),count()).
    
    Performance:tuples are generally more memory effiecient and faster proceses compared to lists
    beacause of thier immutabiltiy. this can be benificial when dealing larage collections of data
    that don't need to modified. lists being mutable , may require more memory and can be slower for
    certain operations.
     14. How do you type a tuple value that only contains the integer 42?

# In[14]:


my_tuple=(42,)


# In[15]:


my_tuple

In Python, to define a tuple with a single element, you need to include a comma after the element. Without the comma, Python would interpret the parentheses as regular parentheses, and the value inside would not be considered a tuple. By adding the comma, you explicitly indicate that you want to create a tuple.15. How do you get a list value's tuple form? 
    In python in order to convert list values from tuple
    we use tuple() function.
# In[16]:


my_list=[1,2,3,4,5,6]
my_tuple=tuple(my_list)
my_tuple

16. Variables that "contain" list values are not necessarily lists themselves. Instead,
    what do they contain?
    
    Variable that 'contains' list values in python actually contains references to the
    list objects when you assign a list to a varaible, the variable does not hold directly list data itself.
    In Python, objects such as lists are stored in memory, and variables serve as references or pointers to those objects.
    When you assign a list to a variable, the variable becomes a reference to the list object.
    Multiple variables can reference the same list object, allowing for aliasing and shared access to the list data.
    
    Example:
# In[18]:


my_list=[1,2,3,4]
ref_list=my_list

my_list.append(5)
ref_list.append(8)

my_list #1,,2,3,4,5,8
ref_list#1,2,3,4,5,8

17. How do you distinguish between copy.copy() and copy.deepcopy()?

    copy.copy() and deepcopy() function in copy module of python standard libaray.
    
    copy.copy():The functions perform a shallow copy of the objects.It creates a new objects with new reference
    but contents of new object's still same as original object.In case of list shallow copy creates a new list
    objects.but the elements themslves are not copied.
    
# In[20]:


import copy

original_list = [1, [2, 3]]
copied_list = copy.copy(original_list)

original_list[1].append(4)

print(original_list)  # Output: [1, [2, 3, 4]]
print(copied_list)    # Output: [1, [2, 3, 4]]

    deepcopy():copy.deepcopy(): This function performs a deep copy of an object.
    It creates a completely independent copy of the object and all its nested objects. 
     In the case of a list, a deep copy creates a new list object and recursively copies all its elements.
# In[21]:


import copy

original_list = [1, [2, 3]]
deep_copied_list = copy.deepcopy(original_list)

original_list[1].append(4)

print(original_list)      # Output: [1, [2, 3, 4]]
print(deep_copied_list)   # Output: [1, [2, 3]]


# In[ ]:




