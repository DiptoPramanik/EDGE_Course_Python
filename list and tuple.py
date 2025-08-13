marks = [12.4,89.2,56.9,78.4,34.9]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
student = ["dipto",23,"Gaibandha"]
print(student)
student[0]="pritom"
print(student)
print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[-3:-1])

nums = [2,1,3]
nums.append(4)
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)
n = [1,22,2,44,64,23,78,2,1,50]
n.insert(1,50)
print(n)
n.remove(2) #first occur element delete
print(n)
n.pop(1) #indexed element delete
print(n)

#Tuple
tup = (87,64,33,95,76)
print(tup[0])
# tup[0]=98 #not allowed
print(type(tup))
print(tup)
tup =() #empty tuple
print(type(tup))
tup = (1,) #single value 
print(type(tup))
tup = (1)
print(type(tup))
tup =(1,2,3,4,) #tup =(1,2,3,4)
print(type(tup))

#tuple slicing
tup =(1,2,3,4,5)
print(tup[1:4])

tup = (2,1,3,1)
print(tup.index(1))
print(tup.count(1))

#WAP to ask the user to enter names of their 3 favorite movies and store them in a list
a = input("Enter your favorite Movie Name : ")
b = input("Enter your favorite Movie Name : ")
c = input("Enter your favorite Movie Name : ")
movie_list = []
movie_list.append(a)
movie_list.append(b)
movie_list.append(c)
print(movie_list)

#WAP to check if a list contains a palindrome of elements.
nums = [1,2,3,2,1]
duplicate_nums = nums.copy()
duplicate_nums.reverse()
if (duplicate_nums==nums):
    print("Palindrome")
else:
    print("Not")

#WAP to count the number of students with the "A" Grde in the following tuple.
tup = ("c","D","A","A","B","B","A")
print(tup.count("A"))

#store the above values in a list and sort them from "A" to "D"
li = ["c","D","A","A","B","B","A"]
li.sort()
print(li)

