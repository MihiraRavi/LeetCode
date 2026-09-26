202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1

class Solution:
    tracker_list = []
    def split_digits(self, m: int) -> list:
        num_list = []
        while m > 0 :
            digit = m % 10
            num_list.append(digit)
            m = m // 10
        return num_list
    def isHappy(self, n: int) -> bool:
        digit_list = self.split_digits(n)
        sum = 0
        for i in digit_list :
            sum += (i ** 2)
        if sum == 1 :
            self.tracker_list.clear()
            return True
        else :
            if sum in self.tracker_list :
                self.tracker_list.clear()
                return False
            else :
                self.tracker_list.append(sum)
                return self.isHappy(sum)
