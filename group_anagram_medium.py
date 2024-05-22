# Question : (link - https://leetcode.com/problems/group-anagrams/description/)
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


# Solution : 


class Solution(object):
    def groupAnagrams(self, strs):

        # Solution 1 : time complexity O(m*n)
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return res.values()

        # Solution 2 : sorting O(m * nlogn)

        res = defaultdict(list)
        for s in strs:
            word = "".join(sorted(s))
            res[word].append(s)
        return res.values()