# 1143. Longest Common Subsequence
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

# from typing import str

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[0]*len(text1)
        longest=0

        for c in text2:
            curr_length=0
            for i, val in enumerate(dp):
                if curr_length < val:
                    curr_length=val
                elif c==text1[i]:
                    dp[i]=curr_length+1
                    longest=max(longest, curr_length+1)
        return longest


test=Solution()
text1 = "abcde"
text2 = "ace"
print(test.longestCommonSubsequence(text1,text2)) # 3 'ace'

text1="oxcpqrsvwf"
text2="shmtulqrypy"
print(test.longestCommonSubsequence(text1,text2)) # 2 'qr'
