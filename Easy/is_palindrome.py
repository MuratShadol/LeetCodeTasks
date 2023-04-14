"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

"""

def isPalindrome(self, s):
    s = str(s)
    s = "".join(filter(str.isalnum, s)).lower()
    point1, point2 = 0, len(s) - 1
    while point1 <= point2:
        if s[point1] != s[point2]:
            return False
        point1 += 1
        point2 -= 1
    return True
