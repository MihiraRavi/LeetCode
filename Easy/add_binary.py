"""
67. Add Binary
Easy

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na = len(a) - 1
        nb = len(b) - 1
        diff = abs(na - nb)
        if diff != 0 :
            extraZeros = "" + ("0" * diff)
            if na < nb :
                a = extraZeros + a
            else :
                b = extraZeros + b
        result = []
        carry = 0
        for i in range(len(a) - 1, -1, -1) :
            sumab = int(a[i]) + int(b[i]) + carry
            result.insert(0, sumab % 2)
            carry = sumab // 2
        if carry != 0 :
            result.insert(0, carry)
        return "".join(map(str, result))
