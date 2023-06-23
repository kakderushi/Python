#!/usr/bin/env python
# coding: utf-8
1.) In Python, what is the difference between a built-in function and a user-defined function? 
     Provide an example of each.
     
     Built-In_Function:
     Built-in functions are pre-defined functions that are provided by the Python programming language itself. 
     They are readily available for use without requiring any additional code or imports.
     These functions are part of the Python standard library and cover wide range of task
     example:(print(),len(),type())
 
# In[1]:


#python built-in-function
print("hellow world")

ser-defined Function:
    User-defined functions are created by the users themselves to perform specific tasks according to their requirements. 
    These functions are defined using the def keyword, followed by a function name, parentheses for optional parameters, and 
    a colon. The function body is indented and contains the code to be executed when the function is called.
    User-defined functions can be reused throughout the program, making the code more modular and maintainable.
    
# In[3]:


def Myfunc():
    print("hellow wrold")
Myfunc()

2.) How can you pass arguments to a function in Python? Explain the difference between positional arguments and keyword arguments
    
    In python there are couple of ways to pass arguments to a function:
  1)Positional arguments:
    Positional arguments are passed to a function based on their position or order. 
    The values you provide in the function call are assigned to the parameters of the function in the order they appear.
    The number and order of arguments must match the function defination:

# In[4]:


def greet(name,age):
    print("hello",name)
    print("You are ",age ,"years old")
greet("rushi",21)

2)Keyword arguments:
    Keyword arguments are passed to a function using the parameter names explicitly. Instead of relying on the position,
    you specify the parameter name followed by a colon (:) and the value. This allows you to pass arguments in any order, 
    even skipping some arguments if they have default values.
    

# In[6]:


def greet(name,age):
    print("hellow",name)
    print("You age is",age,"years old")
greet(name="rushi",age=21)

3.)  What is the purpose of the return statement in a function? Can a function have multiple return statements? 
     Explain with an example.
     
     The return statement in a function is used to specify the value that the function should return when it is called.
     It allows the function to provide a result or output that can be used by the code that called the function.
     The return statement also terminates the function execution, meaning any code after the return statement within 
     the function will not be executed.

     A function can have multiple return statements. However, only one return statement is executed, 
     and it determines the value that is returned. Once a return statement is encountered, the function immediately exits, and 
     the value specified by the return statement is passed back to the caller
# In[30]:


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

student_score = 85
grade = get_grade(student_score)
print("Grade:", grade)


4.) What are lambda functions in Python? How are they different from regular functions? Provide an example where
    a lambda function can be useful
    
    
    Lambda functions, also known as anonymous functions, are small, single-expression functions in Python. 
    They are defined using the lambda keyword, followed by a list of parameters, a colon (:), 
    and the expression to be evaluated. Lambda functions are often used when a simple, one-line function is required without 
    the need for a formal function definition.

The main differences between lambda functions and regular functions are as follows:

    Syntax: Lambda functions have a compact syntax compared to regular functions.
    They are defined using the lambda keyword, whereas regular functions are defined using the def keyword.

     Anonymous: Lambda functions are anonymous because they don't require a function name. 
     They are typically used where the function logic is simple and only needs to be used in a specific context.

    Single expression: 
    Lambda functions are restricted to a single expression. They can only contain a single line of code,
    which is evaluated and returned as the result. In contrast, regular functions can have multiple statements and a
    more complex structure.
    


# In[10]:


# Sorting a list of tuples based on the second element using a lambda function

students = [("Alice", 23), ("Bob", 20), ("Charlie", 21), ("David", 19)]

# Sorting the students list based on the second element of each tuple
students.sort(key=lambda x: x[1])

print(students)

5.) How does the concept of "scope" apply to functions in Python? Explain the difference between local scope and global scope.

    The concept of "scope" in Python defines the accessibility and visibility of variables within different parts 
    of a program. It determines where a variable can be accessed or referenced. In Python, scope is defined by
    the block structure, primarily by functions, and it helps maintain variable integrity and prevent naming conflicts.

There are two main types of scope in Python:

  1)Local Variable:
    Local variable refers to the postion of the code where a variable is defind inside the function, They are not vissible
    outside the function and cannot be accessible other part's of program. When the function is exceuted ,the local
    varibles are created, and they exists only until the function compltes its exeution.
    
# In[11]:


#local variable 
def myFunction():
    x=10
    print(x)
myFunction()

 Exaplanation of above code:
 In this above code we defined 'x' variable inside the myFunction() so scope of this varaible is only for this function.
 we cannot acceses this variable outside the function.
     2)Global Variable:
   Global variable refers to the position of the code where a variable is defind outside the function or top level of the
   module. variable definds in the function we can use it any parts of the program. or outside the function. 
   They can be accessed and modified by any function or code block within the program.
# In[12]:


#Global variable
x=10
def myFunction():
    print(x)
myFunction()

Exaplanation of above code:
In this code we defined 'x ' as variable outside the function but still we use it within the function because this type
of variable is global.6. How can you use the "return" statement in a Python function to return multiple values?
    
    In python you are use return statement to return multiple values by separating with commons.
    Way of returning multiple values:
    
    1)Returning values as tuple:
      returning values as tuple simply listing values by separated commons after return statement:
    
# In[13]:


#returning values as tuple:
def myFunction():
    x=10
    y=20
    z=30
    return x,y,z
result=myFunction()
print(result)

    2)Returning values as list or any data structure:
      Instead of using tuple , we use list or other any data structure for returning multiple values
# In[14]:


#returning values as list of any data structure
def myFunction():
    x=10
    y=20
    z=30
    return [x,y,z]
result=myFunction()
print(result)

7. What is the difference between the "pass by value" and "pass by reference" concepts when it comes to function arguments in Python?
 
 Python does not strictly adhered the concept of pass by value and pass by refernce in function arugments. instead of it
 Python uses a mechanism called "pass by object reference" or "pass by assignment."
 
Pass by Value:
In languages that use pass by value, when a function is called, the values of the arguments are copied into the function's parameters. Any modifications made to the parameters within the function do not affect the original values of the arguments outside the function. Essentially, the function works with copies of the original values.

Pass by Reference:
In languages that use pass by reference, when a function is called, the references (or memory addresses) of the arguments are passed to the function's parameters. This means that any modifications made to the parameters within the function directly affect the original values of the arguments outside the function. The function works with the actual variables passed to it.
 
 
 In python:
    Python uses a mechanism called "pass by object reference" or "pass by assignment." When a function is called, 
    the references to the objects (variables) are passed to the function as arguments. However,
    whether the function modifies the original object or not depends on the mutability of the object and how
    the object is accessed within the function.
    
Immutable Objects (Pass by Value-like behavior):
    Immutable objects such as numbers (integers, floats), strings, and tuples cannot be modified once created.
    When passed as arguments to a function, their values are copied into the function's parameters. 
    Any modifications made to these parameters within the function do not affect the original objects outside the function. 

# In[15]:


def modify_number(num):
    num += 10

x = 5
modify_number(x)
print(x)  #5

Mutable Objects (Pass by Reference-like behavior):
Mutable objects such as lists, dictionaries, and sets can be modified after creation. When passed as arguments to a function, their references are copied into the function's parameters. Any modifications made to these parameters within the function can affect the original objects outside the function.
# In[20]:


def modify_list(lst):
    lst.append(4)
    
my_list=[1,2,3]
modify_list(my_list)
print(my_list)#[1,2,3,4]

8. Create a function that can intake integer or decimal value and do following operations:
a. Logarithmic function (log x)
b. Exponential function (exp(x))
c. Power function with base 2 (2x) 
d. Square root
# In[26]:


import math

def perform_operations(x):
    logarithm = math.log(x)
    exponential = math.exp(x)
    power = math.pow(2, x)
    square_root = math.sqrt(x)
    
    return logarithm, exponential, power, square_root
result = perform_operations(3.5)
logarithm_result, exponential_result, power_result, square_root_result = result

print("Logarithm:", logarithm_result)
print("Exponential:", exponential_result)
print("Power (base 2):", power_result)
print("Square Root:", square_root_result)

9.)Create a function that takes a full name as an argument and returns first name and last name.
# In[29]:


def myData(fullName):
    names=fullName.split()
    frist_name=names[0]
    last_name=names[-1]
    return frist_name,  last_name
res=myData("Rushikesh kakde") 
frist_name,last_name=res
print('frist_name:',frist_name)
print('last_name:',last_name)
    
     


# In[ ]:




