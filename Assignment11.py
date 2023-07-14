#!/usr/bin/env python
# coding: utf-8
1.) What is the role of the 'else' block in a try-except statement? Provide an example scenario where it would be useful.The role of 'else block' in a try except block, it will executed when the try block of code is not rasie any type of error
then the else part of the code is exceuted.

# In[1]:


try:
    x=int(input("enter the num1"))
    y=int(input("enter the num2"))
    res=x/y
    print(res)
except ZeroDivisionError:
    print("we cannot divide a number by zero!")
else:
    print("It will work in right way !")

In above example we can see it after try block of code is succesesfully executed, then it aslo executed else part of the program.2.) Can a try-except block be nested inside another try-except block? Explain with an example.Yes, we can use try except block nested inside another try-except block this called as nested exception handling,
It allows to handle different level of exception  at differnet different level of code execution.
# In[2]:


try:
    #outer try 
    try:
        #inner try block
        numerator=int(input("enter the numerator"))
        denomintor=int(input("enter the denomintor"))
        res=numerator/denomintor
        print(res)
        #inner except block
    except ZeroDivisionError:
        print("we cannot divide numerator by zero")
        #outer except block
except:
    print("suppose any eerror occured in the try block")
        

In above example we can see, we used to nested try-except block ,Frist we use outer try then we use inner try after that we used
inner except block and outer except block.3. How can you create a custom exception class in Python? Provide an example that demonstrates its usage.To create custom exception in python, you need to define new class that inherits the built-in 'exception' 
class or any subclasses this custom class can be raise or handle exception.

# In[5]:


class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def divide_numbers(a, b):
    if b == 0:
        raise CustomException("Division by zero is not allowed.")
    return a / b


try:
    result = divide_numbers(10, 0)
    print("Result:", result)
except CustomException as e:
    print("Error:", e)

In this example, we create a custom exception class called CustomException that inherits from the built-in Exception class. The CustomException class has an __init__ method to initialize the exception with a custom error message, and a __str__ method to define the string representation of the exception when it is printed.

We then define a function called divide_numbers that takes two arguments and performs division. If the second argument is zero, it raises an instance of the CustomException class with a specific error message.

In the try block, we call the divide_numbers function with arguments 10 and 0, which triggers the CustomException to be raised. The except block catches the CustomException and assigns it to the variable e, allowing us to access the error message using e.message. In this case, it will print "Error: Division by zero is not allowed."

By creating a custom exception class, you can define specific types of exceptions that are meaningful in the context of your application and handle them accordingly.
4. What are some common exceptions that are built-in to Python?TypeError: Raised when an operation or function is performed on an object of inappropriate type.

ValueError: Raised when a function receives an argument of the correct type but an invalid value.

NameError: Raised when a local or global name is not found.

IndexError: Raised when a sequence subscript is out of range.

KeyError: Raised when a dictionary key is not found
.
FileNotFoundError: Raised when a file or directory is not found.

IOError: Raised when an input/output operation fails.

ZeroDivisionError: Raised when division or modulo operation is performed with zero as the divisor.

AttributeError: Raised when an attribute reference or assignment fails.


ImportError: Raised when an import statement fails to find the module or function.

TypeError: Raised when an operation or function is performed on an object of inappropriate type.

OverflowError: Raised when the result of an arithmetic operation is too large to be expressed within the given numeric type.

MemoryError: Raised when an operation fails due to lack of memory.

StopIteration: Raised to signal the end of an iterator.

KeyboardInterrupt: Raised when the user interrupts the execution, typically by pressing Ctrl+C.


These are just a few examples of the many built-in exceptions available in Python. Each exception provides specific information about the type of error that occurred, allowing you to handle them appropriately in your code.
5. What is logging in Python, and why is it important in software development? Logging in Python is a built-in module that allows you to record status, progress, and error messages during the execution of a   program. It provides a flexible and configurable way to collect and store log messages for analysis and debugging purposes.
 Logging is important in software development for several reasons:

Debugging and troubleshooting: Logging helps in identifying and diagnosing issues by providing a detailed record of the program's execution. When unexpected errors occur, log messages can provide valuable information about the state of the program, variable values, and the sequence of events leading to the error.

Monitoring and maintenance: Logging allows developers to monitor the health and performance of an application in production. By logging relevant information, such as resource usage, processing times, and critical events, developers can identify bottlenecks, track performance trends, and optimize the application as needed.

Auditing and compliance: Logging can be used for auditing purposes, especially in systems that handle sensitive data or require compliance with certain regulations. By logging relevant actions and events, you can track user interactions, system activities, and detect any unauthorized access or suspicious behavior.

Understanding user behavior: Logging can provide insights into how users interact with an application. By logging user actions, preferences, and usage patterns, you can analyze the data to improve user experience, identify popular features, and make data-driven decisions for future development.

Error reporting: Logging allows you to capture and report errors systematically. By logging exceptions, stack traces, and relevant contextual information, you can generate error reports that help in understanding and resolving issues reported by users.

Documentation and historical records: Logging serves as a historical record of events and activities within an application. It can help in documenting the behavior of the software, tracking changes, and providing a timeline of actions for future reference.
6. Explain the purpose of log levels in Python logging and provide examples of when each log level would be appropriate.Log levels in Python logging define the severity or importance of a log message. They help in categorizing and filtering log messages based on their significance, allowing developers to control the verbosity and detail of logging output. Python's logging module provides the following built-in log levels:

DEBUG: The lowest log level used for detailed diagnostic information. It is typically used during development and debugging stages to provide fine-grained information about the program's execution, variable values, and intermediate steps. Example: Logging detailed function call information for troubleshooting complex issues.

INFO: A general informational message to indicate the normal flow of the program. It gives a high-level overview of the application's progress and important milestones. Example: Logging when the application starts or stops, or providing summary information about the program's state.

WARNING: An indication of a potential issue or something that could lead to an error in the future. It highlights abnormal or unexpected events that don't necessarily cause the program to fail but require attention. Example: Logging deprecated function usage or non-critical configuration warnings.

ERROR: A message indicating a significant problem or error that occurred during the program's execution. It signifies that an operation or functionality couldn't be completed successfully but doesn't necessarily terminate the program. Example: Logging an exception that was caught and handled, or recording an error in an external service call.

CRITICAL: The highest log level used to indicate a critical failure or error that requires immediate attention. It typically results in the termination of the program or a severe impact on the system. Example: Logging a database connection failure or a security breach attempt.

# In[6]:


import logging

# Configure the logging
logging.basicConfig(level=logging.DEBUG)

# Create a logger
logger = logging.getLogger("my_logger")

# Log messages with different levels
logger.debug("This is a debug message")      # Detailed diagnostic information
logger.info("This is an info message")       # General informational message
logger.warning("This is a warning message")  # Indication of a potential issue
logger.error("This is an error message")      # Signifies a significant problem
logger.critical("This is a critical message") # Indicates a critical failure

7. What are log formatters in Python logging, and how can you customise the log message format using formattersLog formatters in Python logging allow you to customize the format of log messages. They define the structure and content of the log output, including the timestamp, log level, message, and any additional information you want to include.

Python's logging module provides a default log formatter, but you can create your own custom formatter or modify the default formatter to suit your specific requirements.

To customize the log message format using formatters, you can follow these steps:

Import the logging module: Start by importing the logging module in your Python script or module.
# In[7]:


import logging

Create a formatter instance: Instantiate a logging.Formatter object to define the format of the log messages.
# In[8]:


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

%(asctime)s: Inserts the timestamp of the log message.
%(levelname)s: Inserts the log level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
%(message)s: Inserts the actual log message.
You can customize the format by adding or removing placeholders and adding any desired text or formatting.Create a handler and assign the formatter: Create a logging handler (such as StreamHandler, FileHandler, etc.) and associate the formatter with it.
# In[9]:


handler = logging.StreamHandler()
handler.setFormatter(formatter)

In this example, a StreamHandler is created to output log messages to the console. You can use different handlers depending on your needs (e.g., FileHandler to write to a file).Create a logger and add the handler: Create a logger instance and add the handler to it.
# In[10]:


logger = logging.getLogger('my_logger')
logger.addHandler(handler)

Log messages using the logger: Use the logger to log messages at different log levels.logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
The log messages will be formatted according to the formatter specified earlier.

By customizing the log message format using formatters, you have control over how the log messages are structured, 
what information is included, and how it is presented. This allows you to tailor the logging output to meet your specific needs, making it easier to read, analyze, and troubleshoot the logged information.8. How can you set up logging to capture log messages from multiple modules or classes in a Python application?To Capture logging to capture log messages from multiple modules or classes in a python application
we use python logging module. The logging module provides :
# In[2]:


#import the logging module
import logging

#configure the logging system

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



To create logger instance in each module or class where you want to capture log messages
# In[4]:


logger = logging.getLogger(__name__)

The --name-- variable will be automatically set the module or class where it is called
# In[5]:


#start logging meassageses

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

You can use any of the logging methods (debug, info, warning, error, critical) to log messages at different levels of severity.

Run your Python application and check the output. By default, the log messages will be printed to the console. However, you can configure the logging system to store logs in files or send them to other destinations.
It's important to note that the logging configuration should be performed before any log messages are emitted, typically at the beginning of your application. This ensures that all loggers across different modules or classes use the same configuration.

By following these steps, you can set up logging to capture log messages from multiple modules or classes in your Python application9.) What is the difference between the logging and print statements in Python? When should you use logging over print statements in a real-world application?Destination: The print statement sends output to the standard output stream (usually the console), while logging provides the flexibility to send log messages to various destinations such as the console, files, network sockets, email, or external logging services.

Severity Levels: Logging allows you to categorize log messages with different severity levels (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL). This helps in distinguishing between different types of messages and enables you to filter and handle them differently based on their importance. On the other hand, print statements do not have built-in severity levels.

Flexibility and Configurability: Logging provides a highly flexible and configurable logging system. You can customize the log message format, set the logging level, define multiple loggers, apply filters, and specify handlers to control where the log messages are sent. This configurability is particularly useful in large applications with multiple modules and classes. With print statements, you have limited control over the output format and destination.

Debugging and Troubleshooting: Logging is especially useful for debugging and troubleshooting purposes. You can selectively enable or disable logging for specific modules or classes, allowing you to focus on relevant log messages. Additionally, you can configure logging to capture detailed information such as timestamps, loggers' names, and stack traces, which can aid in diagnosing issues. Print statements, while helpful for basic debugging, lack the advanced features and flexibility provided by the logging module.10. Write a Python program that logs a message to a file named "app.log" with the following requirements: 
● The log message should be "Hello, World!" 
● The log level should be set to "INFO." 
● The log file should append new log entries without overwriting previous ones
# In[6]:


import logging

# Configure the logging system
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Log the message
logging.info("Hello, World!")

The logging.basicConfig() function is used to configure the logging system. We specify the log file name as 'app.log', set the logging level to logging.INFO, and define the format of the log message using format='%(asctime)s - %(levelname)s - %(message)s'. Adjust the log file name and format as needed.
The logging.info() function is used to log the message "Hello, World!" at the INFO level.
When you run this program, it will append the log entry to the "app.log" file without overwriting previous log entries. Each log entry will include the timestamp, log level, and message in the specified format.

Make sure you have write permissions in the directory where the program is executed to create and write to the log file.11. Create a Python program that logs an error message to the console and a file named "errors.log" if an exception occurs during the program's execution. The error message should include the exception type and a timestamp
# In[7]:


import logging
import datetime

# Configure the logging system
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Configure logging to file
file_handler = logging.FileHandler('errors.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger('').addHandler(file_handler)

try:
    # Your program logic here
    # ...
    # Simulate an exception for demonstration
    raise ValueError("An example exception occurred.")

except Exception as e:
    # Log the exception
    error_message = f"{type(e).__name__} - {str(e)}"
    logging.error(error_message)
    print("Exception occurred. Please check the error logs.")

The logging.basicConfig() function is used to configure the logging system. We set the logging level to logging.ERROR to capture only error-level log messages.
A FileHandler is configured to log errors to the "errors.log" file. The file handler is set to the logging.ERROR level and has a specific format for log messages.
The program logic is placed within a try-except block. You should replace the # Your program logic here comment with your actual program code.
Inside the except block, the exception is caught, and the error message is constructed by combining the exception type (type(e).__name__) and the exception message (str(e)).
The error message is logged using logging.error() to both the console and the "errors.log" file.
A message is printed to the console to indicate that an exception occurred.
When you run this program and an exception occurs, it will log the error message to both the console and the "errors.log" file. The error message will include the exception type, the exception message, and the timestamp.

Ensure that you have write permissions in the directory where the program is executed to create and write to the log file.
