"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

def isValid(s):
    stack = []
    hashset = {')': '(', ']': '[', '}': '{'}
    for par in s:
        if par in hashset:
            if stack and stack [-1] == hashset[par]:
                stack.pop()
            else:
                return False
        else: 
            stack.append(par)
    return True if not stack else False
