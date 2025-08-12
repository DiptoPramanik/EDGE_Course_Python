print("Hello World !!")
print("Dipto Kumer Pramanik.","From Rangpur")
print(23)
print(20+30)

# Variable
name = "dipto"
age = 26
cgpa = 3.40
print("NAME : ",name)
print(cgpa)
age2 = age
print("AGE : ",age2)
print(type(name))

# DataType
name1 = "dk"
name2 = '''dk'''
name3 = 'dk'
is_okay = True
a = None
print(type(a))

# Arithmatic Operation
a = 3
b = 2
sum = a+b
print(sum)

diff = a-b
print(diff)
print(a*b)
print(a/b)
print(a%b) #reminder
print(a**b) #a^b


# single line commments
"""
Multiple Line 
        comments

"""
# relational Operators
a = 20
b = 50
print(a==b)
print(a!=b)
print(a<=b)
print(a>b)
print(a<b)
print(a>=b)

# assignment operator
num = 2
# num = num +10
num+=10
print(num)
num-=10
print(num)
num*=10
print(num)
num/=10
print(num)
num%=10
print(num)
num**=5
print(num)

# logical operators
print(not False)
a = 20
b = 5
print(not (a>b))
print("and operator : ",(a==b) and (a>b))
print("or operator : ",(a==b) or (a>b))

# type conversion
a,b = 2,2.5
sum = a + b 
print(sum)

# type casting
a = "2"
b = 3.5
a = int(a)
print(a+b)

# input taking
name = input("Enter Your Name : ")
print("you are welcome",name)
age  = int(input("Enter your Age : "))
print("your age is : ",age)
val  = float(input("Enter a floating value : "))
print(val)

#Write a program to input 2 numbers and print their sum
val1 = int(input("Enter your first value : "))
val2 = int(input("Enter your second value : "))
print(val1 + val2)

#WAP to input side of a square and print its area 
side = int(input("Enter a Side : "))
print(side**2) 
# print(side*side)

#WAp to input 2 floating point numbers and print their average
a  = float(input("enter a number : "))
b  = float(input("enter a number : "))
sum = a+b
print(sum/2)

#WAP to input 2 integer numbers ,a and b
# print True if a is greater or equal to b.If not print False
x  = int(input())
y = int(input())
print(a>=b)


