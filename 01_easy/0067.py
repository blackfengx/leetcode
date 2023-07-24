# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Empty String to return result
        res = ""

        # Variable to use for carry on Binary Addition
        carry = 0

        # During Addition, I want to start at rightmost number,
        # So I use this line of code to "flip" the order of string
        # A and B.
        a, b = a[::-1], b[::-1]

        # Will iterate the number of times of the longest string
        for i in range(max(len(a), len(b))):

        # Checking if current index is "in bounds", else 0, also converts
        # index into an integer.
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2

        # Puts a 1 in front of res if there is a carry.
        if carry:
            res = "1" + res


        return res
