#!/usr/bin/env python
# coding: utf-8
1.) What is the primary goal of Object-Oriented Programming (OOP)?
     
     The primary goal of object-oriented programming (OOP) is a model the real world in a software application by 
     using objects and their interactions, OOP is paradigm that organizes data and behavior into self contained
     units called objects which are instances of the classes.
     
     Key objectives of OPP are:
     Encapsulation:
     Encapsulation is the bundling of data and methods that operate on the data within single unit , the object 
     It allows the object to control it internal state and provides a clear interface for interacting with it,
     hiding the implementation of outside world . This helps in reducing complexity and making code more manegeable
     
     Abstraction:
     Abstraction is the proceses of simplifying complex reality by modeling classes and objects that represent
     entities and their characteristics. It allows progrmmaers to focus on relvent attributes and behaviours
     while ingonring unnecessary details. This makes it easier to design understand and modify the code.
     
     Inheritance:
     Inheritance is a mechanism that allows a class (The subclass or derived class) to inherit properties 
     and behaviors form another class .This promotes code reusability .
     
     Polymorphism:
     Polymorphism enables objects of diffrent classes to be treated as objects of common superclass
     this allows methods to be defined in the superclass and overriden(use) in the subclass, providing a consistent
     interface to diffrent object's polymorphism simplifies code and makes it more adaptable to varing data and behavior.
     
    2. What is an object in Python?

     In Python , an objcet is fundamental concept that represents a specific instances of data structure or user defined class.
     Everything on python is object, including simple data types like string , intergers and even more complex data types
     are aslo objects.
     
     An object in python have two main characteristics:
     
     Identity:
     Each object has a unique indentity which like unique address or identifier for that specific objects,
     we think of it is memory location where of it as stored . The id() function in python can be used to get
     the indentity of the object.
     
     state and Behavior:
     object have both state and behavior. In python state represent attribute's means variable which hold the data.
     and behavior represent method's  which is a function we can also call it.
     
     when you create an object, In python allocates memory to store its attributes and methods
     and each object has its own set of these attributes methods. This allows you to have multiple
     instances of the same class. each with its own unique state and the ability to execute methods
     independetly.
     
     
     
# In[1]:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_hello(self):
        print(f"hello my name is {self.name} and my age is {self.age}")
    


# In[2]:


#creating objects of this class
person1=Person("rushieksh",21)


# In[3]:


#calling the methods on the object
person1.say_hello()

In the above example , person1 is object of the Person class 
here we create an object of the person class. and it has own unique state(name and age) 
and methods (say_hello)3. What is a class in Python?
   In python, a class is blueprint or a template that defines the structure and behavior of object's it is a fundamental 
   concept of object oriented programming (OOP) which allows you to create object's with specific data member and methods
   (functions) that operate those attributes . classes serve as way to organize and encapsulate related data and
   functionality into a single unit.
    
# In[4]:


class ClassName:
    #class attribute (shared by all instances of the class)
    class_attribute=value
    #constructor (aslo called intializer)
    def __init__(self,arg1,arg2):
        #instance attributes (specific to each instance of the class)
        self.instance_attr1=arg1
        self.insance_attr2=arg2
        
        
        #instance methods
        def method1(self,...):
        #method code
        def method2(self,..):
            
    

Break down all components:

class: This keyword is used to define the class

className: the class name should start with letter of __ underscore with our convinence

class attribute:These are variables defined directly within the class

__init__: This is the constructor method that gets called when you create an instance of the class.

self: self is keyword which is refers to the current instance of the object.

instances attributes: These are specific to each instance of the class and hold differnt values for each object.

instances methods:These functions defined within the class and can be operate instance attributes of the class.

# In[ ]:


#creating an instance of the class
obj=ClassName(arg1 value,arg2 value)
#calling the instance methods
obj.method1
obj2.methid2
#accessing the instance attributes
print(obj.instance_attribute1)

class provide a powerful way to model real world entitis and create modular reusable code 
in python.4. What are attributes and methods in a class?
    
    In a class , attribute are vairbale that store data associated with instances of the class
    and methods are functions that define the behavior of the class and can operate on those
    attributes. Attributes and methods are defined within the class and are accessed using the dot
    notation with instances of the class.
    
    Attribute:
    Attribute can be classified into two types:
    1) Class Attribute:
        class attribute are defined directly within the class and are shared by all instances of the class.
        they are accessed using the class name and are the same for all objects of that class.
        class attribute are typically used for values that are constant across all instances.
        
# In[5]:


class MyClass:
    class_attribute="this is class attribute"
   


# In[6]:


#Accesssing class attribute
MyClass.class_attribute

    2) instance attributes:
       instance attributess are specific to each instance (object) of the class. 
       They are intialized and assigned values in the constructor
       (__init__) method using the self keyword
        instance attributes represnt the unique data for each object .
# In[7]:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

#creating instance of the class
person1=Person("rushi",12)
person2=Person('sanket',23)
person1.name


# In[8]:


person2.age

Methods: 
methods are functions defined within a class and operate on the class's attributes 
they can be classified into two types:

1)Instance Methods:
  Instance methods  take the self parameter as the frist argument which refers to the instance
  invoking the method.
  These methods can access and modify instance attributes.
  instance methods are used to perform operations specific to individual instances of the class
  
# In[9]:


class Calcualtor:
    def __init__(self):
        self.result=0
    def add(self,num):
        self.result+=num
    def multiply(self,num):
        self.result*=num
        
#creating an instance of the class
cal=Calcualtor()
cal.add(5)


# In[10]:


cal.result


# In[11]:


cal.multiply(12)


# In[12]:


cal.result

2)class methods:
  class method are decorated with @classmethod and take cls parameter as the frist arugment which
  refers to the class itself.
  they can be accessed and modify class attributes but not instance attributes sicne
  do not have access to specific instance data
  class methods are used when you want perform operations that affects the entire class, not 
  just individual instances.
# In[13]:


class MyClass:
    class_attribute=0
    @classmethod
    def increment_class_attribute(cls):
        cls.class_attribute+=1
        
#using class method


# In[14]:


MyClass.increment_class_attribute()
MyClass.class_attribute

5. What is the difference between class variables and instance variables in Python?

    Difference between class methods and instance varibales:
    Instance variable:
    Instance variable are specific to each instance (object) of the class.
    They are initialized and assigned values in the constructor (__init__) methods using self keyword.
    Instance attribute represent the unique data for each object.
    
    class variables:
    class varaibles are defined within the class and shared by all instances of the class
    They are accessed using the class name and are same for objects of that class.
    class variables are typically used for values that are constant across all instance.
    6. What is the purpose of the self parameter in Python class methods

    Purpose of the self parameter in python class methods:
    Self keyword is used as parameter in constructor or methods.
    self keyword is refer to the current instance of the class.
    self keyword is specify each instance of the class.
    without self keyword in methods, this methods treated as class attributes, so 
    it can shared common values for all attributes in class.
# In[15]:


class Person:
    #here we used self keyword as parameter 
    #to shared unique data for each instance
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show(self):
        print(f"My name is {self.name} and I am {self.age} year old")
        


# In[16]:


person1=Person("Rushikesh",21)


# In[17]:


person1.show()

7. For a library management system, you have to design the "Book" class with OOP principles in mind. The “Book” class will have following attributes: 
a. title: Represents the title of the book.
b. author: Represents the author(s) of the book.
c. isbn: Represents the ISBN (International Standard Book Number) of the book.
d. publication_year: Represents the year of publication of the book.
e. available_copies: Represents the number of copies available for checkout. 
The class will also include the following methods:a. check_out(self): Decrements the available copies by one if there are copies available for checkout.
b. return_book(self): Increments the available copies by one when a book is returned.
c. display_book_info(self): Displays the information about the book, including its attributes and the number of 
   available copies.

# In[59]:


class Book:
    def __init__(self,title,author,isbn,publication_year, available_copies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.publication_year=publication_year
        self.available_copies=available_copies 
        
        #checkout 
    def check_out(self):
        if self.available_copies>=1:
                return self.available_copies-1  
            
    def display_book_info(self):
        print(f"Title of my book {self.title} and it's author is {self.author} it's isbn {self.isbn} and its publication year is  {self.publication_year} available_copies : {self.available_copies}")  
        
    def return_book(self):
        return self.available_copies+1
    
    #creating object of the class
    
    book1=Book('Rich dad poor dad','Robert kiyosaki',12,2018,10)


# In[60]:


book1.check_out()


# In[61]:


book1.display_book_info()


# In[62]:


book1.return_book()

8. For a ticket booking system, you have to design the "Ticket" class with OOP principles in mind. 
The “Ticket” class should have the following attributes: 

a. ticket_id: Represents the unique identifier for the ticket.
b. event_name: Represents the name of the event.
c. event_date: Represents the date of the event. 
d. venue: Represents the venue of the event.
e. seat_number: Represents the seat number associated with the ticket.
f. price: Represents the price of the ticket. 
g. is_reserved: Represents the reservation status of the ticket.


The class also includes the following methods:
a. reserve_ticket(self): Marks the ticket as reserved if it is not already reserved.
b. cancel_reservation(self): Cancels the reservation of the ticket if it is already reserved. 
c. display_ticket_info(self): Displays the information about the ticket, including its attributes and reservation status.
# In[75]:


class Ticket:
    def __init__(self,ticket_id,event_name,event_date,venue,seat_number,price,is_revserved):
        self.ticket_id=ticket_id
        self.event_name=event_name
        self.event_date=event_date
        self.venue=venue
        self.seat_number=seat_number
        self.price=price
        self.is_revserved=is_revserved
    def reserve_ticket(self):
        if self.ticket_id==1234:
            print(f"My reservation is succesesful {self.ticket_id}")
           
    def cancel_reservation(self):
        if self.ticket_id==909:
                print("oops can not reserved")
        
        
    def display_ticket_info(self):
        print(f"My ticket id is :{self.ticket_id} event name is {self.event_name} and it organised in {self.event_date}venue is {self.venue} my seat number is : {self.seat_number} and it is  price {self.price} and status of reservation {self.is_revserved}")


# In[76]:


ticket1=Ticket(909,'ganesh chaturthi','13th augest','pune',345,100,'yes')


# In[77]:


# calling method for reserving ticket
ticket1. reserve_ticket()


# In[78]:


#calling method for cancelation of ticket
ticket1.cancel_reservation()


# In[80]:


#calling the function for display infromation about attributes and methods
ticket1.display_ticket_info()

9. You are creating a shopping cart for an e-commerce website. Using OOP to model the "ShoppingCart" functionality the class should contain following attributes and methods:
a. items: Represents the list of items in the shopping cart.

The class also includes the following methods:

a. add_item(self, item): Adds an item to the shopping cart by appending it to the list of items.
b. remove_item(self, item): Removes an item from the shopping cart if it exists in the list. 
c. view_cart(self): Displays the items currently present in the shopping cart.
d. clear_cart(self): Clears all items from the shopping cart by reassigning an empty list to the items attribute.

# In[97]:


class ShoppingCart:
    def __init__(self,item):
        self.item=item
        
    def add_item(self,item):
        print(f"here  we add item: {self.item}")
    
    def remove_item(self,item):
        print(f"removed item {self.item}")
    
    def view_cart(self):
        print(self.item)
    
    def clear_cart(self):
        print(self.item)


# In[98]:


#creating object of the class
shop=ShoppingCart('camera')


# In[99]:


#here we add item 
shop.add_item('tv')


# In[100]:


#here we add item
shop.add_item('phone')


# In[101]:


#here we view the item
shop.view_cart()


# In[102]:


#here we remove the item
shop.remove_item('phone')


# In[103]:


#here we clear add items
shop.clear_cart()

10. Imagine a school management system. You have to design the "Student" class using OOP concepts.The “Student” class has the following attributes:
a. name: Represents the name of the student. 
b. age: Represents the age of the student.
c. grade: Represents the grade or class of the student.
d. student_id: Represents the unique identifier for the student.
e. attendance: Represents the attendance record of the student.

The class should also include the following methods:
a. update_attendance(self, date, status): Updates the attendance record of the student for a given date with the provided status (e.g., present or absent).
b. get_attendance(self): Returns the attendance record of the student.
c. get_average_attendance(self): Calculates and returns the average attendance percentage of the student based on their attendance record.
# In[160]:


class Student:
    def __init__(self,name,age,grade,student_id,attendance):
        self.name=name
        self.age=age
        self.grade=grade
        self.student_id=student_id
        self.attendance=attendance
    def update_attendance(self,date,status):
        if self.student_id=='A-60':
            print(f"attendance of the student in: {date} and status of the student: {status}")
       
    def get_attendance(self):
           if self.attendance=='yes':
                print(self.attendance)
        
    def get_avg_attendance(self):
        if self.attendance=='yes':
            print(f"average percentage of attendance of a student {self.attendance}")
           


# In[161]:


stud=Student("Rushieksh",21,'A','A-60','yes')


# In[162]:


stud.update_attendance('12th augest','present')


# In[163]:


stud.get_attendance()


# In[164]:


stud.get_avg_attendance()


# In[ ]:




