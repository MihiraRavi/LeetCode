"""
258. Add Digits

Easy

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
 

Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution:
    def split_digits(self, m: int) -> list:
        num_list = []
        while m > 0 :
            digit = m % 10
            num_list.append(digit)
            m = m // 10
        return num_list
    def addDigits(self, num: int) -> int:
        if num == 0 :
            return 0
        if num < 10 :
            return num
        n_list = self.split_digits(num)
        while len(n_list) > 1 :
            sum = 0
            for i in n_list :
                sum += i
            if sum >= 10 :
                n_list = self.split_digits(sum)
            else :
                return sum
