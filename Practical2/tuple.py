# https://github.com/ChhabhaiyaDevanshi/python_pra2/blob/main/tuple_practical2.py
# 20CE011-CHHABHAIYA DEVANSHI

# ::tuples::

# ---------------------->que-1: Write a Python program to create a tuple with different data types.<--------------------------
# mytuple = ("name", 30, True, "city") #create tuple with diff data types
# print(mytuple, type(mytuple)) 

# ---------------------->que-2: Write a Python program to create a tuple with numbers and print one item.<--------------------------

# tuple = (12, 4.5, 25)
# print(tuple[1]) #print item at index 1

# ---------------------->que-3: Write a Python program to add an item in a tuple.<--------------------------

# thistuple = ("kiwi", "apple", "orange")
# print(thistuple)
# x = list(thistuple) #convert tuple into list
# x.append("banana") #add item using append()
# thistuple = tuple(x) #convert list int tuple
# print(thistuple)

# ---------------------->que-4: Write a Python program to convert a tuple to a string.<--------------------------

# def coverttostring(tup):  #fun to convert a tuple into string
#     str = ' '
#     for item in tup:
#         str = str+item  #add items one by one into str variable 
#     return str


# thistuple = ("a", "p", "p", "l", "e")
# str = coverttostring(thistuple)
# print(str)

# ---------------------->que-5: Write a Python program to find the length of a tuple.<--------------------------

# thistuple = ("apple", "name", 12, 5.6)
# print(len(thistuple)) #len() to find length of tuple
