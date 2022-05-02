

# def swap_ele(lis):
#     tmp=[]
#     maxi = max(lis)
#     print(lis)
#     for i in range(len(lis)):
#         if i <= len(lis) and lis[i] == lis[i+1]:
#             tmp.append(maxi)
#         elif  i<= len(lis) and lis[i+1]!= max :
#             tmp.append(maxi)
#         elif  i<= len(lis) and  lis[i+1]== max :
#             tmp.append(maxi)
#
#         elif i == len(lis):
#             tmp.append(0)
#
#     return tmp
#
# swap_ele([3,4,2,12,3,1])

# def getUniqueCharacter(s):
#     # Write your code here
#     tmp = []
#     index = []
#
#     for i in s:
#         if i not in tmp:
#             tmp.append(i)
#
#         elif i in tmp:
#             pass
#
#     for j in range(len(tmp)):
#         if tmp[j] in s:
#             index.append(s.index(tmp[j]))
#         else:
#             index.append(-1)
#
#     return index[0]
#
# print(getUniqueCharacter("amait"))

import sys
"Use sys.getsizeof() method to find size of any variable, i.e. Number of bytes required by python to store it in memory." \
"Output in bytes"
# var = "a"
# print(sys.getsizeof(var))

"Size of Boolean"

"Python boolean variable requires minimum 24 bytes on 32-bit / 64-bit system. It may vary as per hardware."
#
# print(sys.getsizeof( bool())) # prints 24
# print(sys.getsizeof(True)) # prints 28
# print(sys.getsizeof(False)) # prints 24

# Size of Int
# Python int variable requires minimum 24 bytes on 32-bit / 64-bit system. It may vary as per hardware.

# Find size of int

import sys

print(sys.getsizeof( int())) # prints 24
print(sys.getsizeof(0)) # prints 24
print(sys.getsizeof(1)) # prints 28
print(sys.getsizeof(-2)) # prints 28
print(sys.getsizeof(2* 10**307)) # prints 164
