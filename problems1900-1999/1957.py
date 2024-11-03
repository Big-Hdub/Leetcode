# 1957. Delete Characters to Make Fancy String

# A fancy string is a string where no three consecutive characters are equal.
# Given a string s, delete the minimum possible number of characters from s to make it fancy.
# Return the final string after the deletion. It can be shown that the answer will always be unique.

# Example 1:
# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".

# Example 2:
# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".

# Example 3:
# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".

# Constraints:
# 1 <= s.length <= 105
# s consists only of lowercase English letters


def makeFancyString(s: str) -> str:
    # If the string length is less than 3, it's already fancy
    if len(s) < 3:
        return s

    res = ''  # List to store the resulting characters
    count = 1  # Counter for consecutive characters

    res += s[0]   # Add the first character to the result

    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1  # Increment count if the current character is the same as the previous one
        else:
            count = 1  # Reset count if the current character is different

        if count < 3:
            res += s[i]   # Add the character to the result if count is less than 3

    return res  # return the resulting string

# Test cases
s = "leeetcode"
print(makeFancyString(s)) # Output: "leetcode"

s = "aaabaaaa"
print(makeFancyString(s)) # Output: "aabaa"

s = "aabaabaabaa"
print(makeFancyString(s)) # Output: "aabaabaabaa"

# Time Complexity: O(n), where n is the length of the string. We iterate through the string once.
# Space Complexity: O(n), where n is the length of the string. We store the resulting characters in a new string.
