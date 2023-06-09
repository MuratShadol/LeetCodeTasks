"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""

def groupAnagrams(strs):
    hashset = {}
    for word in range(len(strs)):
        sorted_word = ''.join(sorted(strs[word]))
        if sorted_word not in hashset:
            hashset[sorted_word] = [strs[word]]
        else:
            hashset[sorted_word].append(strs[word])
    result = [0]*len(hashset.values())
    for i, words in enumerate(hashset.values()):
        result[i] = words
    return result
