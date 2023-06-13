#!/usr/bin/env python
# coding: utf-8
Q.1. What are keywords in python? Using the keyword library, print all the python keywords

       keyworld:Python keyworld are special reserved world that have specific meaning
       purpose and can't be used for anything but those in specific used
# In[1]:


import keyword
all_keyword=keyword.kwlist
print(all_keyword)

Q.2. What are the rules to create variables in python?

    Rule for creating varaible in python:
        1)always start with alphabetical characters orstart with _
        2)Do not start with alphanumeric values
        3)reserved keyword can not be used as a varaible
        4)always follows camelcase naming convention in pythonQ.3. What are the standards and conventions followed for the nomenclature of variables in python
     to improve code readability and maintainability?
             
         ans:
        1)variable names:Use descriptive and meaningful name for varaibles to 
        convey their purpose
        2)constant:use uppercase and lowercase variable name for constant 
        3)indentation:use 4 space indentation in python.This is recomended in python for improving code readability
        4)module name:Use lowercase letters and underscores for module names. 
         Module names should be short, descriptive, and separated by underscores.
Q.4. What will happen if a keyword is used as a variable name?
       If we used keyword as a varaible name in python.
       this line of code of gives me an error.
       error:keyword are not used as a variable name in python
   Q.5. For what purpose def keyword is used?
    
   def keyword :In python we used def keyword for creating a function in python
   using def keyword we write the function name .Q.6. What is the operation of this special character ‘\’?

    '\':This special character used for to creating new line in the code
        also this '\' characters used for divide whole string Q.7. Give an example of the following conditions: 
(i) Homogeneous list
(ii) Heterogeneous set 
(iii) Homogeneous tuple


  (i)Homogeneous list:In python homogenous list contains only single type of data(data type)
# In[2]:


list1=[1,2,3,4,5,5]


# In[3]:


list1

(ii)Heterogeneous set:In python heterogenous set contains different types of data.it could be
   integer,string,float,bool.
# In[4]:


set1={1,"rushikesh",2.0,True,12,"omkar"}
set1

(iii)Homogenous tuple:It contains same type of data.It contains only specific type of data.
# In[5]:


tuple1=(1,2,3,4,5,6,6,7)


# In[6]:


tuple1

Q.8. Explain the mutable and immutable data types with proper explanation & examples
      
         Mutable:Mutable data types are those that can be modified or changed after they are created. 
         This means that the value of a mutable object can be altered without creating a new object. 
         Some examples of mutable data types in many programming languages include lists, sets, and dictionaries. 
         Let's take an example in Python:
# In[7]:


list2=[1,2,3,5,8,10]
list2
list2.append(23)
list2
list2[0]=28
list2

        Inmutable:Immutable data types, on the other hand, are those whose value cannot be changed once they are created.
        This means that any operation that appears to modify an immutable object actually creates a new object with the modified
        value.
         Examples of immutable data types in many programming languages include numbers 
         (integers, floating-point, etc.),strings, and tuples. Let's see an example in Python:
# In[8]:


string="hellow"
string
string2=string+"world"
#here we create new object of string rather than changing the exsiting
string2

Q.9. Write a code to create the given structure using only for loop.
        *
       ***
      *****
     *******
# In[9]:


num_rows = 4

for i in range(num_rows):
    # Print spaces
    for j in range(num_rows - i - 1):
        print(" ", end="")
    
    # Print asterisks
    for k in range(2*i + 1):
        print("*", end="")
    
    # Move to the next line
    print()

Q.10. Write a code to create the given structure using while loop.
    ||||||||| 
     |||||||
      |||||
       |||
        |

# In[16]:


# Set initial variables
row_count = 5  # number of rows
stars = 9  # number of stars in the first row
spaces = 0  # number of spaces at the beginning of each row

while row_count > 0:
    print(' ' * spaces + '|' * stars)  # print the row of spaces and stars
    spaces += 1  # increment the number of spaces by 1 for the next row
    stars -= 2  # decrement the number of stars by 2 for the next row
    row_count -= 1  # decrement the row count



# In[ ]:





# In[ ]:





# In[ ]:




