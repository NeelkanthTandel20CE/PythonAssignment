# 20CE144-Neelkanth Tandel
# https://github.com/NeelkanthTandel20CE/PythonAssignment/blob/main/20ce144_pra_7.py

# Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.The two halves contain the same characters but their frequencies do not match.Your task is simple. Given a string, you need to tell if it is a lapindrome.
# Input:
# 6
# gaga
# abcde
# rotor
# xyzxy
# abbaab
# ababc

# Output:
# YES
# NO
# YES
# YES
# NO
# NO

N = int(input())  # take int num input
string = []

for i in range(N):  # append N values in string var
    string.append(input())

for i in range(N):  # loop for check whether the string is lapidrome
    s = str(string[i])  # convert each element into string
    s1, s2 = '', ''
    l = len(s)  # length of element

    if(l % 2 == 0):  # if the length  of element is even
        s1 = s[:l//2]  # store the first half of string values in s1
        s2 = s[l//2:]  # store the second half of string values in s2

    else:  # if the length of element is odd
        s1 = s[:l//2]  # store the first half of string values in s1
        # store the second half of string in s2 except the middle char
        s2 = s[l//2+1:]

    if sorted(s1) == sorted(s2):  # if sorted strings s1 and s2 are equal the the string is lapidrome
        print("YES")

    else:
        print("NO")
