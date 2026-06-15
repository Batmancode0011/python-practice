"""info ={
    "name" : "manish",
    "cgpa" : 9.6,
    "marks" : [97,98,95],
    "subjects" : ("physics","java","c")

}"""
0

"""
print(type(info))
print(info)
print(info["subjects"])"""
"""info ["name"] = " Manish Kumar"# to change previous value to this comand
info["surname"] = "Kumar"# for this command add a new key in the dictonary 
nulldict = {} # to create a new empty dict 
nulldict["name"] = "anchal"# To add new key in empty dict we use this 
print(info)"""

# NESTED Dictionaries 
"""Dictionary ke ander dictionary """
"""student = {
    
    "name" : "manish kuamr",
    "subjects": {
        "physivs" : 95,
        "python" : 98,
        "maths" : 99,
    }
}

print(student)# for print full student dict
print(student["subjects"])# for print only subjects
print(student["subjects"]["maths"])# for only print maths marks"""



#SET
"""
collection = {1,2,3,3,4,5,4,"hello", "world","hello"}
print(collection)
print(len(collection))# total number of items

#collection = set{}# empty set syntax
"""



#Practice Questions

#Q1 store following word meanings in a python dictionary:
"""table : a piece of furniture , lsit of facts& figures
    cat : a small animal"""
#solution

"""dict ={
    "table" : ("a piece of furniture","lsit of facts& figures"),
    "cat" : "a small animal"

}
print(dict)
"""
#Q2 you are given a list of subject for student.
# assume one classroom is requires for 1 subject .
# how many classrooms are needed by all students.
# "python","java","c++","python","javascipt","java","python","java","c++","c".

# solution
"""
subjects = ["python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"]

unique_subjects = set(subjects)

print("Unique Subjects:", unique_subjects)
print("Classrooms needed:", len(unique_subjects))
"""
#Q3 WAP to enter marks of 3 subjects gfrom th euseer and store them in a dict.
# Start with an empty dict & add one by one. 
# Use subject name as key & marks as value.


#solution 

"""
marks= {}

x= int(input("enter phy : "))
marks.update({"phy" : x})

y= int(input("enter chem : "))
marks.update({"chem" : y})

z= int(input("enter math : "))
marks.update({"math" : z})

print(marks)
"""

#Q4 Figure out a way to store 9 & 9.0 as seprate values in the set

value = {("int",9), ("float",9.0)}
print(value)