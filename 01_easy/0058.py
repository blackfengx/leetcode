# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:
    # Input: s = "Hello World"
    # Output: 5
    # Explanation: The last word is "World" with length 5.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_word = 0
        x = s.strip()

        for i in range(len(x)):
            if x[i] == " ":
                last_word = 0
            else:
                last_word +=1
        return last_word
