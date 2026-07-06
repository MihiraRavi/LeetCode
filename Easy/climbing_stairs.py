"""
70. Climbing Stairs

Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        y = n + 1
        a, b = 0, 1
        for i in range (2, y + 1) :
            a, b = b, a + b      
        return b

# fibonacci inefficient recursion 

class Solution:
    def climbStairs(self, n: int) -> int:
        if (n <= 0) :
            return 0
        elif (n == 1) :
            return 1
        elif (n == 2) :
            return 2        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

