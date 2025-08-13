dict ={
    "name" : "dipto",
    "cgpa" : 3.4,
    "marks" : [98,97,99],
    "is_adult" : True,
    "topics" : ("dictionary","tuple"),
    12 : "dipto"
}
print(dict)
print(dict["name"])
dict["name"] = "pritom"
print(dict)
# Empty Dictionary
null_dict = {}
# Nested Dictionary
stduent = {
    "name" : "dipto",
    "subjects" : {
        "phy" : 98,
        "chem": 99,
        "math":95
    }
}
print(stduent)
print(stduent["subjects"])
print(stduent["subjects"]["math"])

# methods
print(dict.keys())
print(list(dict.keys())) #list typecast
print(len(list(dict.keys()))) 
print(dict.values())
print(list(dict.values()))
print(dict.items())
print(list(dict.items()))
pairs = list(dict.items())
print(pairs[0])
print(dict.get("name"))
print(dict["name"])
# print(dict["name1"]) #error
print(dict.get("name1")) #no error-->None
my_dict = {"city":"Rangpur","age":23}
stduent.update(my_dict)
print(stduent)

# Sets
collection ={1,2,1,3,"dipto"}
print(type(collection))
print(collection)
print(len(collection))
null_set = set() # empty set
null_set.add(3)
null_set.add(2)
null_set.add(6)
null_set.add(2)
null_set.add((1,2,3))
null_set.add("dipto")
print(null_set)
null_set.remove(2)
print(null_set)
null_set.pop() #print randomly removed value 
print(null_set)
null_set.clear()
print(null_set)

set1 = {1,2,3}
set2 ={3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))

#Store following word meaning in apython dictionary
dict ={
    "table":["a piece of furniture","list of facts& figures"],
    "cat":"a small animal"
}
print(dict)

#You are given of subjects for students.Assume one classroom is required for 1 subject.How many classrooms are needed by all students.
languages = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(languages))
#WAP to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary & add one by one.Use subject name as key & marks as value.
marks={}
x = int(input("Enter Physics mark : "))
marks.update({"phy":x})
y = int(input("Enter chemistry mark : "))
marks.update({"chem":y})
z= int(input("Enter Math mark : "))
marks.update({"math":z})
print(marks)
#Figure out a way to store 9 & 9.0 as separated values in the set.
#simple way
values ={"9",9.0}
print(values)
values = {("float",9.0),("int",9)}
print(values)