# 3163. String Compression III

# Given a string word, compress it using the following algorithm:

# Begin with an empty string comp. While word is not empty, use the following operation:
# Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
# Append the length of the prefix followed by c to comp.
# Return the string comp.

# Example 1:

# Input: word = "abcde"
# Output: "1a1b1c1d1e"

# Explanation:

# Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.
# For each prefix, append "1" followed by the character to comp.

# Example 2:

# Input: word = "aaaaaaaaaaaaaabb"
# Output: "9a5a2b"

# Explanation:

# Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.
# For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
# For prefix "aaaaa", append "5" followed by "a" to comp.
# For prefix "bb", append "2" followed by "b" to comp.

# Constraints:
# 1 <= word.length <= 2 * 105
# word consists only of lowercase English letters.

class Solution:
    def compressedString(self, word: str) -> str:
        """
        Compresses the input string by counting consecutive occurrences of each character.

        Args:
            word (str): The input string to be compressed.

        Returns:
            str:    The compressed string where each sequence of the same character is
                    replaced by the count of characters followed by the character itself.

        Example:
            compressedString("aaabbc") -> "3a2b1c"
        """
        compressed_string = ""  # Initialize the compressed string
        count = 0  # Initialize the count of consecutive characters
        curr_char = word[0]  # Initialize the current character to the first character of the word

        for i, char in enumerate(word):
            if char == curr_char:
                count += 1  # Increment the count if the current character matches the previous one
                if count == 9:  # If count reaches 9, append it to the compressed string
                    compressed_string += f"{count}{char}"
                    if i + 1 < len(word):
                        curr_char = word[i + 1]  # Update the current character
                    count = 0  # Reset the count
            else:
                compressed_string += f"{count}{curr_char}"  # Append the count and character to the compressed string
                count = 1  # Reset the count to 1 for the new character
                curr_char = char  # Update the current character

        if count > 0:
            compressed_string += f"{count}{curr_char}"  # Append the remaining count and character to the compressed string

        return compressed_string

solution = Solution()

word = "abcde"
print(solution.compressedString(word))  # Output: "1a1b1c1d1e"

word = "aaaaaaaaaaaaaabb"
print(solution.compressedString(word))  # Output: "9a5a2b"

word = "aaaaaaaaay"
print(solution.compressedString(word))  # Output: "9a1y"

word = "yyyyyyyyfffccccqqwwffffffffrrrrrrrrraaaaayyyyyyyyy"
print(solution.compressedString(word))  # Output: "8y3f4c2q2w8f8r5a9y"

# Space Complexity: O(n)
# The space complexity is O(n) because we are storing the compressed string, which in the worst case can be as long as the input string where
# a 1 is in front of every character if there are no repeating characters.

# Time Complexity: O(n)
# The time complexity is O(n) because we are iterating through the input string once.
