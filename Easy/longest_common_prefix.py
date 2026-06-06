"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        lcp = ""
        minlen = 200
        for s in strs :
            minlen = min(minlen , len(s))
        for i in range(minlen) :
            c = strs[0][i]
            for j in range(1, n) :
                if strs[j][i] != c :
                    return lcp
            lcp = lcp + c
        return lcp

# code avoiding the initial loop

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # number of strings
        n = len(strs)
        # longest common prefix
        lcp = ""
        # if empty array , nothing to do
        if n == 0 :
            return lcp
        # lcp cannot be more than the lenght of the first string 
        # i is index of the first and subsequent words
        for i in range(len(strs[0])) :
            # i th letter of the first strig 
            # all strings must have c in i th position for c to be in lcp
            c = strs[0][i]
            # loop through all strings except first
            for j in range(1, n) :
                # suppose j th word is smaller than first word
                # then cannot check further
                if len(strs[j])) <= i:
                    return lcp
                # when characters are different, no need to check further 
                if strs[j][i] != c :
                    return lcp
            # if control reaches here, it means that all strings have same charater at position i
            # so, c is part of lcp
            lcp = lcp + c
        return lcp
     
