def calculate_sum(a,b):
    # sum = a+b
    # print(sum)
    # return sum
    return a+b

sum = calculate_sum(2,3)
print(sum)

def print_hello():
    print("Hello")

print_hello()

def print_hello():
    print("Hello")

output = print_hello()
print(output)

#average 3 numbers
def cal_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    return avg

res = cal_avg(1,2,3)
print(res)

#Default parameters
def calc_prod(a=2,b=4):
    print(a*b)
    return (a*b)

calc_prod()

def calc_prod(a,b=4):
    print(a*b)
    return (a*b)

calc_prod(3)

# def calc_prod(a=2,b): error  
#     print(a*b)
#     return (a*b)

# calc_prod()

# WAF to print the length of a list
cities = ["Dhaka","khulna","Rangpur","Gaibandha","Barishal"]
fruits = ["apple","banana","cherry","orange"]

def print_length(list):
    print(len(list))

print_length(cities)
print_length(fruits)

# WAF to print the elements of a list in a single line.
def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(fruits)
print()
# WAF to find the factorial of n
def factorial(n):
    fact=1
    for it in range(1,n+1):
        fact*=it
    return fact

res = factorial(5)
print(res)

#WAF to convert USD to TAKA
def usd_converter(dollar):
    taka = dollar*121.58
    return taka
output = usd_converter(2)
print("TAKA = ",output)

#Recursion
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
    # print("END")
show(5)

#Factorial
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
    
res = fact(5)
print(res)

#Write a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if(n==1):
        return 1
    else:
        return n+calc_sum(n-1)
print(calc_sum(5))
# # another way
# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1) + n
# sum  = calc_sum(5)
# print(sum)

#Write a recursive function to print all elements in a list
def print_list(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits =["mango","lichi","banana","cherry","apple"]
print_list(fruits,0)