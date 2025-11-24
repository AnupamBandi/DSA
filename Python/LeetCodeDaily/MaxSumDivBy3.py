# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

 

# Example 1:

# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
# Example 2:

# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
# Example 3:

# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).

from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        if total % 3 == 0:
            return total
        
        # rem1 = []
        # rem2 = []

        # # Separate numbers by remainder
        # for n in nums:
        #     if n % 3 == 1:
        #         rem1.append(n)
        #     elif n % 3 == 2:
        #         rem2.append(n)

        # # Sort the remainder buckets
        # rem1.sort()
        # rem2.sort()

        # candidates = [0]

        # # If total % 3 == 1 → remove one (mod1) OR two (mod2)
        # if total % 3 == 1:
        #     if rem1:
        #         candidates.append(total - rem1[0])
        #     if len(rem2) >= 2:
        #         candidates.append(total - rem2[0] - rem2[1])

        # # If total % 3 == 2 → remove one (mod2) OR two (mod1)
        # else:
        #     if rem2:
        #         candidates.append(total - rem2[0])
        #     if len(rem1) >= 2:
        #         candidates.append(total - rem1[0] - rem1[1])

        # return max(candidates)

    # or
        r11 = 10000
        r12 = 10000
        r21 = 10000
        r22 = 10000
    
        for n in nums:
            if n %3 == 1 and n < r12:
                if n < r11:
                    r11 = r12
                    r12 = n
                else:
                    r11 = n    
            if n % 3 == 2 and n < r22:
                if n < r21:
                    r22 = r21
                    r21 = n
                else: 
                    r22 = n
        
        if total % 3== 1:
            return total - min(r12,r21+r22)
        else:
            return total - min(r21,r12+r11)
    

def main():
    sol = Solution()

    # Example test case
    nums = [3, 6, 5, 1, 8]
    result = sol.maxSumDivThree(nums)

    print("Input:", nums)
    print("Max sum divisible by 3:", result)
    
    
    # dp = [0,float('-inf'),float('-inf')]
    #     for n in nums:
    #         newdp = dp[:]
    #         r = n%3
    #         for rem in range 3:
    #             new_rem = (rem+r)%3
    #             newdp[new_rem] = max(newdp[new_rem],newdp[rem]+ n)
    #         dp = newdp
    #     return dp[0]


if __name__ == "__main__":
    main()
