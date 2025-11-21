// # 1930. Unique Length-3 Palindromic Subsequences

// # Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

// # Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

// # A palindrome is a string that reads the same forwards and backwards.

// # A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

// # For example, "ace" is a subsequence of "abcde".
// # Example 1:

// # Input: s = "aabca"
// # Output: 3
// # Explanation: The 3 palindromic subsequences of length 3 are:
// # - "aba" (subsequence of "aabca")
// # - "aaa" (subsequence of "aabca")
// # - "aca" (subsequence of "aabca")
// # Example 2:

// # Input: s = "adc"
// # Output: 0
// # Explanation: There are no palindromic subsequences of length 3 in "adc".
// # Example 3:

// # Input: s = "bbcbaba"
// # Output: 4
// # Explanation: The 4 palindromic subsequences of length 3 are:
// # - "bbb" (subsequence of "bbcbaba")
// # - "bcb" (subsequence of "bbcbaba")
// # - "bab" (subsequence of "bbcbaba")
// # - "aba" (subsequence of "bbcbaba")

class Solution {
    countPalindromicSubsequence(s) {
        const letters = new Set(s);
        let ans = 0;

        for (const letter of letters) {
            const i = s.indexOf(letter);
            const j = s.lastIndexOf(letter);

            if (i < j) {
                const between = new Set();
                for (let k = i + 1; k < j; k++) {
                    between.add(s[k]);
                }
                ans += between.size;
            }
        }

        return ans;
    }

    or 

    countPalindromicSubsequence(s){
        const letters = new Set(s)
        let ans = 0;

        for (const letter of letters){
            const i = s.indexOf(letter)
            const j = s.lastIndexOf(letter)

            if (i != j){
                const between = new Set((s.slice(i+1,j)))
                ans += between.size
            }
        }
        return ans
    }
}


// ---- Test Locally ----
const sol = new Solution();
console.log(sol.countPalindromicSubsequence("aabca")); // Expected 3
