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

# WAF to print 


