# 2490. Circular Sentence

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
# Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

# A sentence is circular if:
# The last character of a word is equal to the first character of the next word.
# The last character of the last word is equal to the first character of the first word.
# For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences.
# However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

# Given a string sentence, return true if it is circular. Otherwise, return false.

# Example 1:

# Input: sentence = "leetcode exercises sound delightful"
# Output: true
# Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
# - leetcode's last character is equal to exercises's first character.
# - exercises's last character is equal to sound's first character.
# - sound's last character is equal to delightful's first character.
# - delightful's last character is equal to leetcode's first character.
# The sentence is circular.

# Example 2:

# Input: sentence = "eetcode"
# Output: true
# Explanation: The words in sentence are ["eetcode"].
# - eetcode's last character is equal to eetcode's first character.
# The sentence is circular.

# Example 3:

# Input: sentence = "Leetcode is cool"
# Output: false
# Explanation: The words in sentence are ["Leetcode", "is", "cool"].
# - Leetcode's last character is not equal to is's first character.
# The sentence is not circular.

# Constraints:
# 1 <= sentence.length <= 500
# sentence consist of only lowercase and uppercase English letters and spaces.
# The words in sentence are separated by a single space.
# There are no leading or trailing spaces.

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Check if the first character of the sentence is the same as the last character
        if sentence[0] != sentence[-1]:
            return False

        # Split the sentence into words
        words = sentence.split()

        # Iterate through the words and check the circular condition
        for i in range(len(words) - 1):
            # Check if the last character of the current word is the same as the first character of the next word
            if words[i][-1] != words[i+1][0]:
                return False

        # If all conditions are satisfied, return True
        return True

# Example test cases
solution = Solution()

# Example 1
sentence1 = "leetcode exercises sound delightful"
print(solution.isCircularSentence(sentence1))  # Output: true

# Example 2
sentence2 = "eetcode"
print(solution.isCircularSentence(sentence2))  # Output: true

# Example 3
sentence3 = "Leetcode is cool"
print(solution.isCircularSentence(sentence3))  # Output: false

# Space Complexity: O(n)
# The space complexity is O(n) where n is the length of the sentence. This is because we are storing the words in a list.

# Time Complexity: O(n)
# The time complexity is O(n) where n is the length of the sentence. This is because we are iterating through the sentence to split it into words and then iterating through the words to check the circular condition.
