# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:

    # Input: s = "III"
    # Output: 3
    # Explanation: III = 3.

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

class Solution(object):
    def romanToInt(self, s):
        total = 0
        for i in range(len(s)):
            if i > 0 and s[i] == "V" and s[i-1] == "I":
                total -= 2
            if i > 0 and s[i] == "X" and s[i-1] == "I":
                total -= 2
            if i > 0 and s[i] == "L" and s[i-1] == "X":
                total -= 20
            if i > 0 and s[i] == "C" and s[i-1] == "X":
                total -= 20
            if i > 0 and s[i] == "D" and s[i-1] == "C":
                total -= 200
            if i > 0 and s[i] == "M" and s[i-1] == "C":
                total -= 200
            if s[i] == "I":
                total += 1
            if s[i] == "V":
                total += 5
            if s[i] == "X":
                total += 10
            if s[i] == "L":
                total += 50
            if s[i] == "C":
                total += 100
            if s[i] == "D":
                total += 500
            if s[i] == "M":
                total += 1000
        return total
