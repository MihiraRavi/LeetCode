"""
119. Pascal's Triangle II

Easy

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pascal_triangle = [[1]]
        if rowIndex == 0 :
            return pascal_triangle[0]
        elif rowIndex == 1 :
            pascal_triangle.append([1,1])
            return pascal_triangle[-1]
        else :
            row_list = [1,1]
            pascal_triangle.append(row_list)
            for i in range(rowIndex - 1) :
                new_row_list = []
                new_row_list.append(1)
                for i in range(len(row_list) - 1):
                    new_row_list.append(row_list[i] + row_list[i+1])
                new_row_list.append(1)
                pascal_triangle.append(new_row_list)
                row_list = new_row_list
                new_row_list = []
            return pascal_triangle[-1]
