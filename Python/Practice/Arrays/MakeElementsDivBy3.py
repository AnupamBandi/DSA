# 3190. Find Minimum Operations to Make All Elements Divisible by Three

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num % 3 != 0:
                count += 1
        return count
    
    # or 
    
    # return sum(num %3 > 0 for num in nums)


# ---- Run & Test Locally ----
if __name__ == "__main__":
    sol = Solution()

    nums = [1, 3, 4, 9]  # Example input
    result = sol.minimumOperations(nums)

    print("Minimum operations:", result)  # Expected output: 2



        