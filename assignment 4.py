# question 1
print("question 1")
from abc import ABCMeta, abstractmethod
class Animal:
   __metaclass__=ABCMeta

   @abstractmethod
   def eat1(self):
      pass
   @abstractmethod
   def eat2(self):
      pass
class Tiger(Animal):
  def eat1(self):
   print("Tiger implementation ...")
class lion(Tiger):
  def eat2(self):
   print("lion implementation ...")
t = lion()
t.eat1()
t.eat2()
# answer 1
# Tiger implementation ...
# lion implementation ...
# question 2
print("question 3")
from abc import ABCMeta, abstractmethod
class AbstractClassExample:
    __metaclass__ =ABCMeta
    def __init__(self, value):
        self.value = value
        super().__init__()
@abstractmethod
def do_something(self):
    pass
class DoAdd(AbstractClassExample):
    def do_something(self):
     return self.value + 42
class DoMul(AbstractClassExample):
    def do_something(self):
        return self.value * 42
x = DoAdd(10)
y = DoMul(10)
print(x.do_something())
print(y.do_something())

# question 3
print("question 3")
def status(age):
  if age < 0:
   raise ValueError("Only positive integers are allowed")
  if age>22:
   print("eligible for mrg")
  else:
   print("not eligible for mrg try after some time")
try:
 num = int(input("Enter your age: "))
 status(num)
except ValueError:
 print("Only positive integers are allowed you ......")
finally:
 print("finally block....")
# answer 3
# Enter your age: 23
# eligible for mrg
# finally block....
# question 4
print("question 4")
class NegativeAgeException(RuntimeError):
 def __init__(self, age):
  super().__init__()
  self.age = age
def status(age):
 if age < 0:
  raise NegativeAgeException("Only positive integers are allowed")
 if age>22:
  print("Eligible for mrg")
 else:
  print("not Eligible for mrg....")
try:
 num = int(input("Enter your age: "))
 status(num)
except NegativeAgeException:
 print("Only positive integers are allowed")
except:
 print("something is wrong")
# answer 4
#Enter your age: 23
# Eligible for mrg
# question 5
print("question 5")
class TooYoungException(Exception):
 def __init__(self,age):
  self.age=age
class TooOldException(Exception):
 def __init__(self,age):
  self.age=age
try:
 age=int(input("Enter Age:"))
 if age<18:
  raise YoungException("Plz wait some time ")
 elif age>65:
  raise TooOldException("Your age too old")
 else:
  print("we will find one girl soon")
except YoungException as e:
  print("Plz wait some time ")
except OldException as e:
  print("Your age too old ")
# answer 5
#Enter Age:2
#Traceback (most recent call last):
# File "C:/Users/Rohit Chaudhary/PycharmProjects/pythonProject/answer check.py", line 15, in <module>
#  except YoungException as e:
#NameError: name 'YoungException' is not defined
# question 6
print("question 6")
try:
  print("outer try block")
  n = int(input("enter a number"))
  print(10/n)
  try:
   print("inner try")
   print("anu"+"preet")
  except TypeError:
   print("Hello")
  else:
   print("inner no exception")
except ArithmeticError:
 print(10/5)
else:
 print("outer no excepiton")
finally:
  print("finally block")
# answer 6
#outer try block
#enter a number4
#2
#inner try
#anupreet
#inner no exception
# outer no excepiton
#finally block
# question 7
print("question 7")
class Person(object):
 def __init__(self, first, last):
  self.firstname = first
  self.lastname = last
 def Name(self):
  return self.firstname + " " + self.lastname
class Employee(Person):
 def __init__(self, first, last, staffnum):
  super().__init__(first,last)
#Person.__init__(self,first, last)
  self.staffnumber = staffnum
 def GetEmployee(self):
  return self.Name() + ", " + self.staffnumber
x = Person("komal", "addanki")
y = Employee("komal", "addanki", "111")
print(x.Name())
print(y.GetEmployee())
# answer 7
#komal addanki
#komal addanki, 111
# question 8
print("question 8")
class Person:
 def __init__(self, first, last):
  self.firstname = first
  self.lastname = last
 def __str__(self):
  return self.firstname + " " + self.lastname
class Employee(Person):
 def __init__(self, first, last, id):
  super().__init__(first, last)
  self.id = id
 def __str__(self):
  return super().__str__()+" "+self.id
x = Person("kamalpreet", "gurpreet")
y = Employee("kamalpreet", "gurpreet", "111")
print(x)
print(y)
# answer 8
#kamalpreet gurpreet
#kamalpreet gurpreet 111
# question 9
print("question 9")
class Vehicle:
 def __del__(self):
  print("Vehicle object destroyed")
  print(10/0)
v = Vehicle()
del v
# answer 9
# Vehicle object destroyed
# question 10
print("question 10")


class Customer:
    def __init__(self, name, bal=0.0):
        self.name = name
        self.bal = bal

    def deposit(self, amount):
        self.bal = self.bal + amount

    def withdraw(self, amount):
        if amount > self.bal:
            raise RuntimeError("withdraw amount is more than balance")
        else:
            self.bal = self.bal - amount

    def remaining(self):
        return self.bal;


c = Customer("Komal", 10000)
damt = int(input("enter amount to deposit"))
c.deposit(damt)
amt = int(input("enter amount to withdraw"))
c.withdraw(amt)
print(c.remaining())
# answer 10
#enter amount to deposit3000
#enter amount to withdraw1000
#12000

