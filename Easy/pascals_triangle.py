"""
118. Pascal's Triangle

Easy

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal_triangle = [[1]]
        if numRows == 1 :
            return pascal_triangle
        elif numRows == 2 :
            pascal_triangle.append([1,1])
            return pascal_triangle
        else :
            row_list = [1,1]
            pascal_triangle.append(row_list)
            for i in range(numRows - 2) :
                new_row_list = []
                new_row_list.append(1)
                for i in range(len(row_list) - 1):
                    new_row_list.append(row_list[i] + row_list[i+1])
                new_row_list.append(1)
                pascal_triangle.append(new_row_list)
                row_list = new_row_list
                new_row_list = []
            return pascal_triangle
