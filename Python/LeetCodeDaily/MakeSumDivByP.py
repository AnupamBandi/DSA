# https://leetcode.com/problems/make-sum-divisible-by-p/description/?envType=daily-question&envId=2025-11-28

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total%p
        if target == 0:
            return 0
        
        mp = {0:-1}
        pref = 0
        res = len(nums)

        for i,x in enumerate(nums):
            pref = (pref+x)%p
            need = (pref - target + p) %p

            if need in mp:
                res = min(res,i-mp[need])
            mp[pref] = i

        return -1 if res == len(nums) else res