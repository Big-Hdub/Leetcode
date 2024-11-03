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
        left,zeros,length,longest=0,0,len(nums),0
        for i in range(length):
            if nums[i]==0:
                zeros+=1
            while zeros>1:
                if nums[left]==0:
                    zeros-=1
                left+=1
            longest=max(longest, i-left+1-zeros)
        return longest-1 if longest==length else longest


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
