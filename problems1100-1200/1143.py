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
        p1,p2,count=0,0,0
        while p1<len(text1) and p2<len(text2):
            if text1[p1]==text2[p2]:
                count+=1
            else:
                for i in range(max(len(text1)-p1, len(text2)-p2)):
                    if len(text2)>p2+i and text1[p1]==text2[p2+i]:
                        count+=1
                        p2+=i
                        break
                    elif len(text1)>p1+i and text2[p2]==text1[p1+i]:
                        count+=1
                        p1+=i
                        break
            p1+=1
            p2+=1
        return count

test=Solution()
text1 = "abcde"
text2 = "ace"
print(test.longestCommonSubsequence(text1,text2)) # 3 'ace'

text1="oxcpqrsvwf"
text2="shmtulqrypy"
print(test.longestCommonSubsequence(text1,text2)) # 2 'qr'
