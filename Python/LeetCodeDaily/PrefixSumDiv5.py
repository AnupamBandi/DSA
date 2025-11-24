# You are given a binary array nums (0-indexed).

# We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

# For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
# Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = 0
        for i in range(len(nums)):
            val = (val*2 + nums[i]) % 5 
            nums[i] = val == 0
        return nums
        
        # val << 1 this will shift left by 1 i.e if the binary is 1 then << 1 will be 10 i.e 2
        # so basically <<1 operator will mutiple value by 2