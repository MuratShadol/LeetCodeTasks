"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

"""

def twoSum(numbers, target):
    point1, point2 = 0, len(numbers)-1 
    while point1 < point2:
        if numbers[point1]+numbers[point2] == target:
            return [point1+1, point2+1]
        elif numbers[point1]+numbers[point2] < target:
            point1+=1
        else:
            point2-=1
