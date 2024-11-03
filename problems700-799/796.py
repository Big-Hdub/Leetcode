# 796. Rotate String

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true

# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false

# Constraints:
# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Determine if one string is a rotation of another string.

        This function checks if the string `goal` can be obtained by rotating the string `s`.
        A rotation involves moving characters from the beginning of the string to the end
        while maintaining their order.

        Args:
            s (str): The original string.
            goal (str): The target string to check if it is a rotation of `s`.

        Returns:
            bool: True if `goal` is a rotation of `s`, False otherwise.
        """
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            if s[i:]+s[:i]==goal:
                return True
        return False

# Test cases
solution = Solution()

print(solution.rotateString("abcde", "cdeab")) # True

print(solution.rotateString("abcde", "abced")) # False

print(solution.rotateString("abcde", "abcde")) # True

print(solution.rotateString("a", "a")) # True

print(solution.rotateString("abc", "acb")) # False

print(solution.rotateString("abcde", "abcd")) # False

print(solution.rotateString("abc", "abcd")) # False

print(solution.rotateString("abcd", "abc")) # False

# Space and Time Complexity
# Time Complexity: O(n^2), where n is the length of the string s. This is because for each character in s, we create a new string of length n.
# Space Complexity: O(n), where n is the length of the string s. This is because we store the concatenated string s[i:] + s[:i] in each iteration.
