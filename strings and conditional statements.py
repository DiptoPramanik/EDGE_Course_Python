str1 = "this is a string"
str2 = 'this is a string'
str3 = """this is a string"""
str = "Now I am learning python basics.\nBecause I will develop some backend engineering tools"
print(str)
str = "Now I am learning python basics.\tBecause I will develop some backend engineering tools"
print(str)
str1  = "Hello"
str2 = "world !!"
# print(str1 + str2)
final_str = str1 + " " +str2
print(len(final_str))

# Indexing
str = "dipto Pramanik"
print(str[1])
# str[1] = 'e'  #not allowed in python

# Slicing
str  = "dipto pramanik"
print(str[1:4])
print(str[:4]) #[0:4]
print(str[4:]) #[4:len(str)]
print(str[-7:-2])

# some functions of string
str = "i am a coder"
print(str.endswith("er"))
print(str.capitalize()) #new string create not change in original String
print(str)
str = "I am a Programmer> Now I am Studying C++"
print(str.replace("C++","Python"))
print(str.replace("a","@"))
print(str.find("Programmer"))
print(str.find("a"))
print(str.count("am"))
print(str.count("a"))

#WAP to input user's first name and print its length
name = input("Enter Your Name : ")
print(len(name))

#WaP to finf the occurrence of 'S' in a String
str = "Sim Siam Syambol "
print(str.count("S"))

# Conditional Stements
age = 16
if (age>=18):
    print("can vote and apply for license")
else:
    print("can't")

light = "green"
if (light=="red"):
    print("Stop")
elif (light=="green"):
    print("go")
else:
    print("look")

# Grade Srudents Based on marks
"""
marks>=90,grade="A"
90>marks>=80,grade="B"
80>marks>=70,grade="C"
70>marks,grade="D"

"""
marks = int(input("Enter Your marks : "))
if marks>=90:
    grade = "A"
elif marks<90 and marks>=80:
    grade = "B"
elif marks<80 and marks>=70:
    grade = "C"
else:
    grade = "D"

print("Your Grade is : ",grade)

# Nested conditional 
age = 75
if (age>=18):
    if(age>=80):
        print("can't Drive")
    else:
        print("Can Drive")
else:
    print("can't Drive")

#WAP to check if a number entered by the user is odd or even
x = int(input("enter a number : "))
if (x%2==0):
    print("EVEN")
else:
    print("ODD")
#WAP to find the greatest of 3 numbers entered by the user
a = int(input("enter a number : "))
b = int(input("enter a number : "))
c = int(input("enter a number : "))
if(a>=b and a>=c):
    print(a)
elif (b>=c):
    print(b)
else:
    print(c)
#WAP to check if a number is a multiple of 7 or not
x = int(input("enter a number : "))
if (x%7==0):
    print("Multiple of 7")
else:
    print("Not Multiple of 7")
