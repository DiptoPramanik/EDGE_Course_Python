#Read a file
f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
# f.close()

#read line by line
line1 = f.readline()
print(line1)

# #Writing to a file
f = open("demo.txt","w")
f.write("this is a new line")

f = open("demo.txt","a")
f.write("this is a new line")

f = open("demo.txt","r+")
f.write("abc")
print(f.read())

f = open("demo.txt","w+")
# f.write("abc")
print(f.read())
f.write("abc")


f = open("demo.txt","a+")
# f.write("abc")
print(f.read())
f.write("abc")

#with syntax
with open("demo.txt","r") as f: 
    data = f.read()
    print(data) 

with open("demo.txt","w") as f: 
    f.write("new data")
   
# deleting a file
import os
os.remove("demo.txt")

#Create a new file "practice.txt" using python.Add the following data in it.
"""
Hi everyone
we are learning File I/O
using java
I like programming in java

"""
with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing java\nI like programming in JAVA")


#WAF that replace all occurences of  "java" with "python" in above file.
with open("practice.txt","r") as f:
    data = f.read()
    new_data = data.replace("java","python")
    print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

#search if the word "learning" exists in the file or not.
def check_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word)!=-1):
            print("found")
        else:
            print("not found")

check_word()
# #WAF to find in cwhich line of the file does the word "learning" occur first.priint -1 if word not found.
def check_for_line():
    word = "learning"
    data = True # valid ->Frue but not valid(space,newline)->False
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1   
    return -1

check_for_line()
#From a file containing numbers separated by comma,print the count of even numbers.
count=0
with open("sample.txt","r") as f:
    data = f.read()
    print(data)
    # num =""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num+=data[i]
    nums = data.split(",")
    # print(nums)
    for val in nums:
        if(int(val))%2==0:
            count+=1

print(count)