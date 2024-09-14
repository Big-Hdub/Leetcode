# 1493. Longest Subarray of 1's After Deleting One Element
# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero1,zero2,length,longest=0,0,len(nums),0
        if nums[0]==1:
            longest=1
        for i in range(length):
            if nums[i]==0:
                if nums[zero2]==1:
                    longest=max(longest,i-1)
                    zero2=i
                elif nums[zero1]==1:
                    longest=max(longest,i-2)
                    zero1=zero2
                    zero2=i
                else:
                    longest=max(longest,i-zero1-2)
                    zero1=zero2
                    zero2=i
            else:
                if nums[zero1]==1:
                    longest=max(longest,i)
                elif nums[zero2]==1:
                    longest=max(longest,i-zero1-1)
                elif i==length-1:
                    longest=max(longest,i-zero1-1)
                else:
                    longest=max(longest, i-1)
        return longest


test=Solution()

nums = [1,1,0,1]
print(test.longestSubarray(nums), 3)

nums = [0,1,1,1,0,1,1,0,1]
print(test.longestSubarray(nums), 5)

nums = [1,1,1]
print(test.longestSubarray(nums), 2)

nums = [1,1,0,0,1,1,1,0,1]
print(test.longestSubarray(nums), 4)

nums = [0,0,0]
print(test.longestSubarray(nums), 0)

nums = [1,0,0,0,0]
print(test.longestSubarray(nums), 1)

nums = [0,1,0]
print(test.longestSubarray(nums), 1)
