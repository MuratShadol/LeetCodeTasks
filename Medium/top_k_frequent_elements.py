"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

"""

def topKFrequent(nums, k):
    hashset = {}
    for idx, val in enumerate(nums):
        if val not in hashset:
            hashset[val] = 1
        else:
            hashset[val] = hashset[val] + 1
    result = [0]*k
    values = sorted(hashset.items(), reverse=True, key=lambda x: x[1])
    for v in range(k):
        result[v] = values[v][0]      
    return result

