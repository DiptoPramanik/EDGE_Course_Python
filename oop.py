# # # # #creating class
# # # # class Student:
# # # #     name = "dipto"

# # # # # creating object
# # # # s1 = Student()
# # # # print(s1.name)
# # # # s2 = Student()
# # # # print(s2.name)

# # # class Car:
# # #     color = "blue"
# # #     brand = "mercedes"

# # # car1 = Car()
# # # print(car1.color)
# # # print(car1.brand)

# # class Student:
# #     # Default constructors
# #     def __init__(self):
# #         pass
# #     college_name = "ABC College" #class attribute
# #     # Parameterized Constructors
# #     def __init__(self,name,marks):
# #         # print(self)
# #         self.name = name
# #         self.marks = marks
# #         # print("adding new students in the database...")
    

# #     def hello(self):
# #             print("Welcome Student, ",self.name)
    
# #     def get_marks(self):
# #          return self.marks

# # s1 = Student("dipto",95)
# # print(s1.name,s1.marks)
# # s2 = Student("pritom",98)
# # print(s2.name,s2.marks)
# # # print(s2.college_name)
# # print(Student.college_name) 
# # s1.hello()
# # print(s1.get_marks())

# #Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average.
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello_guys():
#         print("HELLOOOOO!!!!!!!!!")
#     def get_average(self):
#         sum = 0
#         for val in self.marks:
#             sum+=val
#         print("Hi !!",self.name,"Your average score is : ",sum/3)

# s1 = Student("dipto",[99,98,97])
# s1.get_average()

# s1.name = "pritom"
# s1.get_average()
# s1.hello_guys()


# Abstraction
# class Car:
#     def __init__(self):
#         self.accelerator = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.brk = True
#         self.accelerator = True
#         print("Car Started!!")

# car1 = Car()
# car1.start()

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