"""
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

"""

def generateTheString(n):
    if n % 2 != 0:
        return 'a'*n
    else:
        return 'a'*(n-1) + 'b'
