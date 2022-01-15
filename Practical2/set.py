#https://github.com/NeelkanthTandel20CE/PythonAssignment/blob/main/Practical2/set.py
# 20CE144-Neelkanth Tandel

# ::set::

# ---------------------->que-1: Write a Python program to add member(s) in a set and clear a set<--------------------------

# myset = {"red", "black", "pink"}
# print(myset)
# myset.add("white") #add element into set 
# print(myset)
# myset.clear() #clear all elements from set
# print(myset)

# ---------------------->que-2: Write a Python program to remove an item from a set if it is present in the set<--------------------------

# myset = {"red", "black", "pink", "blue"}
# print(myset)
# myset.remove("pink")
# print(myset)

# ---------------------->que-3: Write a Python program to create an intersection, Union, difference of sets.<--------------------------

# A = {1, 2, 3, 4, 5}
# B = {2, 4, 6, 7, 8, 9}

# print("intersaction:", A & B) 
# print("Union:", A | B)
# print("Difference:", A-B)

# ---------------------->que-4: Write a Python program to find maximum and the minimum value in a set.<--------------------------

# A = {20, 13, 2, 45, 10}
# print(A)
# print(max(A)) #max() to find maximum value in set
# print(min(A)) #min() to find minimum value in set

# ---------------------->que-5: Write a Python program to find the most common elements and their counts from list, tuple, dictionary.<--------------------------

# from collections import Counter
# mylist = ['kiwi', 'apple', 'kiwi', 'orange', 'banana', 'kiwi']
# mydictionary = {
#     "1": "devi",
#     "2": "arya",
#     "3": "nax",
#     "4": "devi",
#     "5": "devi",
#     "6": "nax"
# }
# mytuple = ("apple", "kiwi", "orange", "kiwi", "apple", "apple")

# c = Counter(mylist)
# print("", c.most_common(1))

# a = Counter(mytuple)
# print("", a.most_common(1))

# list1 = mydictionary.items()
# list1 = list(list1)
# print(list1)

# b = Counter(list1)
# print("", b.most_common(1))
