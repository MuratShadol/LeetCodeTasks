"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

def containsDuplicate(nums):
    hashset = {}
    for i in range(len(nums)):
        if nums[i] not in hashset:
            hashset[nums[i]] = True
        else:
            return True
    return False
