#!/usr/bin/env python
# coding: utf-8
Q.1. Create two int type variables, apply addition, subtraction, division and multiplications and store
    the results in variables. Then print the data in the following format by calling the variables: 
    First variable is __ & second variable is __. Addition: __ + __ = __ Subtraction: __ - __ =
    __ Multiplication: __ * __ = __ Division: __ / __ = __ 
# In[12]:


# Create two int variables
first_variable = 10
second_variable = 5

# Perform arithmetic operations and store results
addition_result = first_variable + second_variable
subtraction_result = first_variable - second_variable
multiplication_result = first_variable * second_variable
division_result = first_variable / second_variable

# Print the results in the desired format
print("First variable is", first_variable, "& second variable is", second_variable)
print("Addition:", first_variable, "+", second_variable, "=", addition_result)
print("Subtraction:", first_variable, "-", second_variable, "=", subtraction_result)
print("Multiplication:", first_variable, "*", second_variable, "=", multiplication_result)
print("Division:", first_variable, "/", second_variable, "=", division_result)

Q.2. What is the difference between the following operators:
(i) ‘/’ & ‘//’
(ii)‘**’ & ‘^’

ans:

    (i) The operators '/' and '//' are used for division in Python, but they have different behaviors.

    The '/' operator performs normal division and returns the quotient as a floating-point number. For example, 9 / 2 
    would evaluate to 4.5.

    The '//' operator performs integer division, also known as floor division. It returns the largest integer less than or
    equal to the quotient. For example, 9 // 2 would evaluate to 4.
    
    
    (ii) The operators '**' and '^' are used for exponentiation in Python, but they have different meanings.

    The '**' operator is the exponentiation operator in Python. It raises a number to the power of another number.
    For example, 2 ** 3 would evaluate to 8 (2 raised to the power of 3).

    The '^' operator, on the other hand, is not an exponentiation operator in Python. It is the bitwise XOR operator,
    used for performing bitwise exclusive OR operations on binary representations of numbers.
    It applies the XOR operation to corresponding bits of the operands. For example, 5 ^ 3 would evaluate to 6 
    (binary representation: 0101 ^ 0011 = 0110).Q.3. List the logical operators.
    and: The 'and' operator returns True if both operands are True, otherwise it returns False.

    or: The 'or' operator returns True if at least one of the operands is True, otherwise it returns False.

   not: The 'not' operator is a unary operator that negates the value of its operand.
   It returns True if the operand is False, and vice versa.
    Q.4. Explain right shift operator and left shift operator with examples.
          The right shift operator (>>) shifts the bits to the right by a specified number of positions. 
          It moves each bit to the right by the specified amount and fills the leftmost bits with the sign bit
          (0 for positive numbers,  1 for negative numbers).
     

# In[1]:


num=16
right_shift=num>>2
print(right_shift)

    The left shift operator (<<) shifts the bits to the left by a specified number of positions. 
    It moves each bit to the left by the specified amount and fills the rightmost bits with 0.
# In[2]:


num=4
left_shift=num<<2
print(left_shift)

Q.5. Create a list containing int type data of length 15. Then write a code to check if 10 is present in the list or not.
    
# In[11]:


n=15
list1=[]
for i in range(n):
    list1.append(i)
if 10 in list1:
    print("Present") 
else:
     print("NO")


# In[ ]:





# In[ ]:




