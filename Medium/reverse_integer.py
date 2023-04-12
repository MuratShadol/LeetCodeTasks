"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

def reverse(self, x):
    str_val = str(x)[::-1]
    if str(x)[0] != '-' and int(str_val) > 2**31-1:
        return 0
    if str(x)[0] == '-':
        if int(str(x)[0] + str_val[:-1]) < -2**31:
            return 0
        return int(str(x)[0] + str_val[:-1])
    return int(str_val)
