#!/usr/bin/env python
# coding: utf-8
1.) What is a lambda function in Python, and how does it differ from a regular function?
   
   In Python, Lambda function is anonymous function meaning it is function without name.
   It is created using lambda keyword. followed by set of parameters, colon and expression
   the result of the expression is the return value of the lambda function.
   
   #Lambda parameters:expression.
   
   Diffrence between lambda function and regular function in Python:
   
   1)Syntax:Lambda function have simple syntax as compared to regular function. In regular function it have
      complex syntax as compared to lambda function.
      
   2)Nameless:Lambda function is anonymous function which means without name.but regular function must have 
              function name followed parameters.which make's lambda function different.
      
   3)Function Body:In lambda function have single expression so there is no need to be block of code
               but in regular function it have their own set of code.
       
   4)Return Value: The result of the expression in a lambda function is automatically returned as the output of the function.
                   In regular functions, you need to explicitly use the return statement to specify the return value.2.) Can a lambda function in Python have multiple arguments? If yes, how can you define and use them? 
    
    Yes, In python lambda function have multiple arguments. we can define and use multiple arguments,
    by separated commons in the parameter list's
    
    Example:
    
# In[8]:


add=lambda x,y: x+y
res=(add(4,5))
print(res)

In above example we can clearly see it, x and y are two arguments , which x consists of 4 and y consits of 5.3. How are lambda functions typically used in Python? Provide an example use case
    
    lambda function in python used in that situation where small, tempoary function is required.
    also in case of higher order function like map(), filter() In this higher order
    function accepts two or more arguments,lambda function provide a convient a way without explicitely name.
    
# In[11]:


num=[1,2,3,4,5]
res_value=map(lambda x:x**2,num)
print(list(res_value))

In example lambda function 'lambda x:x**2' is used with map() function to sqaure each element in the num.
The map() applies the lambda function to each element of the iterable('num') and return iterable of the result.
by converting the iterator of the result using list() we can obtain the result.
# In[13]:


num=[1,2,3,4,5,6,7,8]
res_value=filter(lambda x:x%2==0,num)
print(list(res_value))

Lambda function are also commonly used with filter() function. to selectivly filter each element from an iterable
based on condition.4. What are the advantages and limitations of lambda functions compared to regular functions in Python?
   
   Advantage of lambda function:
   1)Concise syntax:lambda function allow to define simple function in compact manner. They are well-suited
     in single line of expression. and eliminating the need of full function body.
     
   2)Readability:lambda function can make a code more readable.here we place the code logic in their
   place. this used in this situation where code logic is simple.
   
   3)Inline Usage: Lambda functions can be defined and used inline, without the need for a separate function name.
     This can be convenient when working with higher-order functions or when a small, temporary function is needed.
     
   Limitations of lambda function:
   
   1)single expression:lambda function are limited to the single expression. which means they cannot used multiple 
   statement inside the funtion. when we need more complex code and logic then lambda function fails.
   
   2)Lack of name:lambda function is anonymous function, which menas it does not have any name. when it comes into 
   error part it is difficult to identify the error beacuse here we don't known name of the function.
   
   3)Limited functionality:lambda function have a single line of expression ,so it is useful for simple and compact
   function but, when we are taking to complex  code of function it fails due to limited functonality.
    5.) Are lambda functions in Python able to access variables defined outside of their own scope? Explain with an example.

    Yes, lambda functions in Python can access variables defined outside of their own scope. 
    This concept is known as "lexical scoping" or "closure." Lambda functions have access to variables in 
    the surrounding scope in which they are defined, including global variables and variables from enclosing functions.
# In[14]:


def multiplier(n):
    return lambda x: x * n

multiply_by_5 = multiplier(5)
result = multiply_by_5(10)
print(result)  # Output: 50

In the example above, the multiplier function takes an argument n and returns a lambda function. The lambda function multiplies its argument x by n. When multiplier(5) is called, it returns a lambda function that multiplies its input by 5.
The lambda function multiply_by_5 captures and remembers the value of n (which is 5) from the surrounding scope of the multiplier function. When multiply_by_5(10) is called, it multiplies 10 by the captured value of n (which is 5), resulting in 50
Here, the lambda function multiply_by_5 accesses the variable n defined in the enclosing scope of the multiplier function, even after the multiplier function has finished executing. This is possible because lambda functions retain references to variables in their enclosing scope, creating a closure.6.) Write a lambda function to calculate the square of a given number.
    
# In[16]:


sqaure=lambda x:x**2
res=sqaure(4)
print(res)

7. Create a lambda function to find the maximum value in a list of integers.
    
   
# In[20]:


import math
list1=[1,2,3,4,5,78,12]

max_value=lambda x:max(x)
res=max_value(list1)
print(res)

8.) Implement a lambda function to filter out all the even numbers from a list of integers
# In[21]:


num=[1,2,3,4,5,6,7,8]
res_value=filter(lambda x:x%2==0,num)
print(list(res_value))

9.) Write a lambda function to sort a list of strings in ascending order based on the length of each string.
    
# In[22]:


strings = ["apple", "banana", "cherry", "date", "elderberry"]

sorted_strings = sorted(strings, key=lambda x: len(x))

print(sorted_strings)


10. Create a lambda function that takes two lists as input and returns a new list containing the common elements between the two lists
# In[23]:


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = lambda x, y: list(filter(lambda element: element in y, x))

result = common_elements(list1, list2)
print(result)  

11. Write a recursive function to calculate the factorial of a given positive integer.
# In[24]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")

12. Implement a recursive function to compute the nth Fibonacci number.
# In[25]:


def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return n - 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
number = 7
result = fibonacci(number)
print(f"The {number}th Fibonacci number is: {result}")

13.) Create a recursive function to find the sum of all the elements in a given list.
# In[26]:


def recursive_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

# Test the function
numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)
print(f"The sum of the list {numbers} is: {result}")


14.)Write a recursive function to determine whether a given string is a palindrome
# In[27]:


def is_palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])

# Test the function
word = "radar"
result = is_palindrome(word)
print(f"The string '{word}' is a palindrome: {result}")


15.) Implement a recursive function to find the greatest common divisor (GCD) of two positive integers.
# In[28]:


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Test the function
num1 = 24
num2 = 36
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")



# In[ ]:




