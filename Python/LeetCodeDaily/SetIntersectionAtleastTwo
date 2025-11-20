# https://leetcode.com/problems/set-intersection-size-at-least-two/description/?envType=daily-question&envId=2025-11-20

from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals first by ascending end, and then by descending start
        intervals.sort(key = lambda x: (x[1], -x[0]))
        
        # Initialize variables
        res = 0
        p1, p2 = -1, -1
        
        # Iterate over the sorted intervals
        for left, right in intervals:
            # Case when current interval's left is greater than the previous right
            if p2 < left:
                p1 = right - 1
                p2 = right
                res += 2
            # Case when current interval's left is greater than or equal to p1
            elif p1 < left:
                p1 = p2
                p2 = right
                res += 1
        
        return res

# Example usage
intervals = [[1, 3], [2, 3], [1, 2], [3, 5]]
sol = Solution()
print(sol.intersectionSizeTwo(intervals))  # Output should be 3


        