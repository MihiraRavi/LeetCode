"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in range(len(s)) :
            if s[i] == "(" or s[i] == "[" or s[i] == "{" :
                l.append(s[i])
            elif s[i] == ")" :
                if len(l) > 0 and l[-1] == "(" :
                    l.pop()
                else:
                    return False
            elif s[i] == "]" :
                if len(l) > 0 and l[-1] == "[" :
                    l.pop()
                else:
                    return False
            elif s[i] == "}" :
                if len(l) > 0 and l[-1] == "{" :
                    l.pop()
                else:
                    return False
        return len(l) == 0



# Alternate Method

class Solution:
    bracketsDict = {"(" : ")", "[" : "]", "{" : "}"}
    reverseBracketsDict = {v: k for k, v in bracketsDict.items()}

    def isValid(self, s: str) -> bool:
        l = []
        for i in range(len(s)) :
            if s[i] in self.bracketsDict.keys():
                l.append(s[i])
            elif s[i] in self.bracketsDict.values() :
                if len(l) > 0 and l[-1] == self.reverseBracketsDict.get(s[i]) :
                    l.pop()
                else:
                    return False
        return len(l) == 0
