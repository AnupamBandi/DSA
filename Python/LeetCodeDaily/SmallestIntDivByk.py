class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0 or k%5 == 0: return -1
        num = 1
        length = 1
        while num%k != 0 and length<=k+1:
            num = num*10 +1
            length+=1
        return length
    
#   res <= k + 1 is a safety bound  and is optional check ...

# it is put in the loop to prevent it from running forever.

# ✔ Why do people add res <= k+1?

# Because:

# We are trying to find a number made of only 1s (repunits) that is divisible by k.

# At most k different remainders are possible when doing % k (from 0 to k-1).

# If you try constructing numbers 1, 11, 111, 1111, ... by repeatedly doing n = n*10 + 1,
# you must find a remainder repetition within the first k+1 steps (Pigeonhole Principle).

# If after k+1 steps you haven’t found remainder = 0, the sequence is cycling and will never hit 0 → no solution.

# ✔ So res <= k+1 means:

# "Try lengths of repunits only up to k+1. If we didn't find one divisible by k by then, give up."
    
    
    
    
#  Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

# Return the length of n. If there is no such n, return -1.

# Note: n may not fit in a 64-bit signed integer.

 

# Example 1:

# Input: k = 1
# Output: 1
# Explanation: The smallest answer is n = 1, which has length 1.
# Example 2:

# Input: k = 2
# Output: -1
# Explanation: There is no such positive integer n divisible by 2.
# Example 3:

# Input: k = 3
# Output: 3
# Explanation: The smallest answer is n = 111, which has length 3.

        