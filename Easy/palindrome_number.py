"""
Given an integer x, return true if x is a 
palindrome, and false otherwise 
"""

def isPalindrome(self, x):
   return (str(x) == str(x)[::-1])
