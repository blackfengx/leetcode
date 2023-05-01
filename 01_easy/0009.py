# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

    # Input: x = 121
    # Output: true
    # Explanation: 121 reads as 121 from left to right and from right to left.

# Constraints:
# -231 <= x <= 231 - 1

# Follow up: Could you solve it without converting the integer to a string?

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
