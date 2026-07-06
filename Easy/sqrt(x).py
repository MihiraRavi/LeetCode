"""
69. Sqrt(x)

Easy

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 :
            return 1
        guess = 0
        while guess**2 < x :
            guess += 1
        if guess**2 == x :
            return guess
        else :
            epsilon = 0.01
            low = 0
            high = x
            guess = (high + low) / 2.0
            while abs(guess**2 - x) >= epsilon :
                if guess**2 < x :
                    low = guess
                else :
                    high = guess
                guess = (high + low) / 2.0
            return int(guess)
