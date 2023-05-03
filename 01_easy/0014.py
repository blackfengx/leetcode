# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
    # Input: strs = ["flower","flow","flight"]
    # Output: "fl"
    # Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

"""
:type strs: List[str]
:rtype: str
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        s1 = min(strs)
        s2 = max(strs)
        
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1
