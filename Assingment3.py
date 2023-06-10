#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('pinfo', 'program')
   
   ans:1) With help of functions we can avoid rewrting the same
			logic or code again and again in a program.

		2)In a single program ,we can call python functions
			anywhere and aslo call multiple times

		3)function increase readability of code

		4)functions are used in python for code reuability.

	

get_ipython().run_line_magic('pinfo', 'called')

	ans:when the function is called then code in function is executed.

3)what statement creates a function
 
	ans:In python we define function with the def keyworld
		then write the function identifier(name)in followed parentheses and a colon.

get_ipython().run_line_magic('pinfo', 'call')

	ans:
		Function:A function is a piece of code which enhanced
					the reusability and modularity of your program.
					It means that a piece of code need not to be used again.
		Function call:A function call means invovking or calling that
						function for execution of code.	

get_ipython().run_line_magic('pinfo', 'scoops')

	ans: Two global scope in python.
		
		one local scope in python.

get_ipython().run_line_magic('pinfo', 'return')
		
	ans:Each call of the function creates new local variables
		and their lifetimes expire when the function return to the caller.


get_ipython().run_line_magic('pinfo', 'expression')

	ans: A return is a value that a function returns to the callling script
		or function when it completes its task.return value any of the string or integer
		floating types of values.
		
8)if a function does not have a return statement,what is the return value of a call to that 
get_ipython().run_line_magic('pinfo', 'function')

	ans:When the function does not any return type value then that type of 
		function always return none type of values.

9)how do you make a function variable refer to the global variable
	ans:when we create to variable inside a function,that varaible
		is local, and can only be used inside that function.to create
		global variable inside a function,you can use global keyworld.

get_ipython().run_line_magic('pinfo', 'None')

	ans: None data o type is own (None type) in python.

get_ipython().run_line_magic('pinfo', 'do')
		
	ans:the sentence import areallyourpetsnamedic can be used
		or the import statement is used to import a module
		or package inside the python.but areallyourpetsnamedic
		module does the exists inside the standard libaries.
		this moduel is third party libaries.
12)if you had a bacon() feature in a spam module, what would you call it
after importing spam

	ans:
        after importing spam module in python:
		import spam
		
		spam.bacon()

get_ipython().run_line_magic('pinfo', 'error')

	ans:
   		To prevent program from crashing when encountering an error.
		Exception handling: use try except blocks to catch and handle
		exceptions. surround the code may raise an exception with try
		block and specify how to handle the exception in corresponding
		except block.This allows the program too gracefully handle errors
		without terminating abrupty.
		syntx:
			try:
         		# code that may raise an exception
			except:ExceptionType:
				#code to handle the exception.


get_ipython().run_line_magic('pinfo', 'clasuse')

     ans: 
 		Purpose of try and except block in python
		try:The try clause in Python is used to enclose a block of code that may potentially raise an exception.
 		It allows you to handle exceptions and prevent them from causing the program to terminate abruptly. 
		The primary purpose of the try clause is to identify and isolate code segments that might generate exceptions.
		
		Except:
			The purpose of the except clause is to define the actions or behavior to be executed when a specific exception occurs.
			 It allows you to gracefully handle exceptions, perform error recovery, or display meaningful error messages to the user.
			 By specifying different except clauses for different exception types, you can handle various exceptions in a tailored manner.

