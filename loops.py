# while True:
#     print("Hello World !!") #infinite loop
count =1
while count<=5:
    print("Hello World")
    count+=1
print(count)

i=1
while i<=5:
    print(i) #print 1 to 5
    i+=1
print('\n')
i=5
while i>=1:
    print(i) #print 1 to 5
    i-=1
#print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
print('\n')
#print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

# print the multiplication table of a number n
n=2
i=1
while i<=10:
    print(n," * ", i ," = ", (n*i))
    i+=1

#print the elements of the following list using a loop.
nums = [1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(nums):
    print(nums[i])
    i+=1
# search a number x in this tuple using loop.
nums = (1,4,9,16,25,36,49,64,81,100)
i=0
x=64
while i<len(nums):
    if x==nums[i]:
        print("found at index",i)
    else:
        print("finding")
    i+=1

nums = (1,4,9,16,25,36,49,64,81,100)
i=0
x=64
while i<len(nums):
    if x==nums[i]:
        print("found at index",i)
        break
    i+=1
#Break
i=0
while i<=5:
    print(i)
    if i==3:
        break
    i+=1

#continue
i=1
while i<=5:
    if i==3:
        i+=1
        continue
    print(i)
    i+=1

#for loop
nums = [1,4,9,16,25,36,49,64,81,100]
for i in nums:
    print(i)

name = "Dipto Pramanik"
for char in name:
    print(char)

#for loop with else
name = "Dipto Pramanik"
for char in name:
    if char=='o':
        print("o found")
        break
    print(char)
else:
    print("END")
#print("END") #it will work all the time but in this break statement for loop with else,else statement will not work
#print the elements of the following list using a loop.
nums = [1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)

# Search a number x in this tuple using loop
nums = (1,4,9,16,25,36,49,64,81,100)
x=49
idx=0
for el in nums:
    if(el ==x):
        print("Number found at index",idx)
        break
    idx+=1

# range(start?stop,step?)
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])

for i in range(5):
    print(i)

# even number
for i in range(2,101,2):
    print(i)
# print numbers from 1 to 100
for i in range(1,101):
    print(i)

#print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

#print the multiplication table of a number n
n=5
for i in range(1,11):
    print(n,' * ',i,' = ',(n*i))

# pass statement
for el in range(10):
    pass

#WAp to find the sum of first n natural numbers
sum=0
n=5
i=0
while i<=n:
    sum+=i
    i+=1
print(sum)

#WAP to find the factorial of first n numbers
fact =1
n=5
for i in range(1,n+1):
    fact*=i
print(fact)