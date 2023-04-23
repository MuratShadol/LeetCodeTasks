"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

"""

def threeSum(nums):
    res = []
    nums = sorted(nums)

    for i, val in enumerate(nums):
        if i > 0 and val == nums[i-1]:
            continue 
        
        l, r = i+1, len(nums) - 1 
        while l < r:
            threeSum = val + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([val, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1 
    return res
