# # # # #creating class
class Student:
    name = "dipto"

# creating object
s1 = Student()
print(s1.name)
s2 = Student()
print(s2.name)

class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)

class Student:
    # Default constructors
    def __init__(self):
        pass
    college_name = "ABC College" #class attribute
    # Parameterized Constructors
    def __init__(self,name,marks):
        # print(self)
        self.name = name
        self.marks = marks
        # print("adding new students in the database...")
    

    def hello(self):
            print("Welcome Student, ",self.name)
    
    def get_marks(self):
         return self.marks

s1 = Student("dipto",95)
print(s1.name,s1.marks)
s2 = Student("pritom",98)
print(s2.name,s2.marks)
# print(s2.college_name)
print(Student.college_name) 
s1.hello()
print(s1.get_marks())

# #Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello_guys():
        print("HELLOOOOO!!!!!!!!!")
    def get_average(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("Hi !!",self.name,"Your average score is : ",sum/3)

s1 = Student("dipto",[99,98,97])
s1.get_average()

s1.name = "pritom"
s1.get_average()
s1.hello_guys()


# Abstraction
class Car:
    def __init__(self):
        self.accelerator = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.brk = True
        self.accelerator = True
        print("Car Started!!")

car1 = Car()
car1.start()

#Create Account class with 2 attribites - balance & account no.
#create methods for debit,credit & printing the balance.
class Account:
    def __init__(self,balance,account_No):
        self.balance = balance
        self.account_No = account_No

    def debit(self,amount):
        self.balance-=amount
        print("TAKA ",amount,"was debited")
        print("Total Balance = ",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("TAKA ",amount,"was credited")
        print("Total Balance = ",self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Account(10000,12345)
# print(acc1.balance)
# print(acc1.account_No)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(45000)


#delete object
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("dipto")
print(s1)
print(s1.name)
# del s1
# print(s1) #error
del s1.name
# print(s1.name) #error


#Private data access
class Account:
    def __init__(self,account_no,account_pass):
        self.account_no = account_no
        self.__account_pass = account_pass

    def reset_pass(self):
        print(acc1.__account_pass) #possible cuz it's inside in the class


acc1 = Account(12345,"abcde")
# print(acc1.__account_pass) not possible from the outside of the class
#but this operation possible 
print(acc1.reset_pass())

class person:
    __name = "anonymous"
    
    def __hello(self):
        print("Hello Person")
    
    def welcome(self):
        self.__hello()

p1 = person()  
# print(p1.__name)  
# print(p1.__hello())  
print(p1.welcome())

#Inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")
    
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("pirus")

# print(car1.start())
print(car1.color)

#Multi-level inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")
    
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type


car1 = Fortuner("diesel")
car1.start()

#Multiple Inheritance
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#Super Method
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stopped")
    
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = ToyotaCar("prius","electric")
print(car1.type)

# classMethod
class Person:
    name = "dipto"

    # def change_name(self,name):
    #     # self.name = name
    #     # Person.name = name
    #     # self.__class__.name = name
    @classmethod
    def change_name(cls,name):
        cls.name = name


p1 = Person()
p1.change_name("pritom")
print(p1.name)
print(Person.name)

# propertyMethod
class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy+self.chem+self.math)/3)+"%"
    # def calc_percentange(self):
    #     self.percentage = str((self.phy+self.chem+self.math)/3)+"%"
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
      
      
st1 = Student(98,97,99)
print(st1.percentage)

st1.phy = 86
st1.calc_percentange()
print(st1.percentage)

#Polymorphism
print(1 + 2) #mathematically calculation 
print("dipto"+"pramanik") #concatanate
print([1,2,3]+[4,5,6]) #merge

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def show_number(self):
        print(self.real,"i +",self.img,"j")

    # def add(self,num2):
    #     newRealNum = self.real + num2.real
    #     newImgNum = self.img + num2.img
    #     return Complex(newRealNum,newImgNum)
    
    def __add__(self,num2):
        newRealNum = self.real + num2.real
        newImgNum = self.img + num2.img
        return Complex(newRealNum,newImgNum)
    

num1 = Complex(1,3)
num1.show_number()
        
num2 = Complex(4,6)
num2.show_number()

# num3 = num1.add(num2)
num3 = num1 + num2
num3.show_number()

"""
Define a Circle class to create a circle with radius r using the constructor.
Define an Area() method of the class Which calculaes the area of the circle.
Define a Perimeter() method of the class which allows you calculate the perimeter of the circle.

"""
class Circle:
    def __init__(self,r):
        self.r = r
    
    def area(self):
        return 3.14*self.r**2
    
    def perimeter(self):
        return 2*3.14*self.r
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

"""
Define a Employee class with attributes roles,department & salary.This class also has
a showDetails() method.
Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

"""
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def ShowDetails(self):
        print("role = ",self.role)
        print("dept = ",self.dept)
        print("salary = ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")

# e1 = Employee("accountant","finance","60,000")
# e1.ShowDetails()
engg1 = Engineer("Dipto",26)
engg1.ShowDetails()

"""
Create a class called Order which stores item & its price.
use Dunder function __gt__() to convey that:
order1>order2 if price of order1>price of order2

"""
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price

odr1 = Order("chips",20)
odr2 = Order("tea",10)
print(odr1>odr2)
        