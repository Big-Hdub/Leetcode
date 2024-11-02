# 2955. Number of Same-End Substrings

# You are given a 0-indexed string s, and a 2D array of integers queries, where queries[i] = [li, ri] indicates a
# substring of s starting from the index li and ending at the index ri (both inclusive), i.e. s[li..ri].
# Return an array ans where ans[i] is the number of same-end substrings of queries[i].
# A 0-indexed string t of length n is called same-end if it has the same character at both of its ends, i.e., t[0] == t[n - 1].
# A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:

# Input: s = "abcaab", queries = [[0,0],[1,4],[2,5],[0,5]]
# Output: [1,5,5,10]
# Explanation: Here is the same-end substrings of each query:
# 1st query: s[0..0] is "a" which has 1 same-end substring: "a".
# 2nd query: s[1..4] is "bcaa" which has 5 same-end substrings: "bcaa", "bcaa", "bcaa", "bcaa", "bcaa".
# 3rd query: s[2..5] is "caab" which has 5 same-end substrings: "caab", "caab", "caab", "caab", "caab".
# 4th query: s[0..5] is "abcaab" which has 10 same-end substrings: "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab".

# Example 2:

# Input: s = "abcd", queries = [[0,3]]
# Output: [4]
# Explanation: The only query is s[0..3] which is "abcd". It has 4 same-end substrings: "abcd", "abcd", "abcd", "abcd".


# Constraints:

# 2 <= s.length <= 3 * 104
# s consists only of lowercase English letters.
# 1 <= queries.length <= 3 * 104
# queries[i] = [li, ri]
# 0 <= li <= ri < s.length

from typing import List

class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        Calculate the number of substrings that start and end with the same character
        for given ranges in the string.

        Args:
            s (str): The input string.
            queries (List[List[int]]):  A list of queries, where each query is a list
                                        containing two integers [li, ri] representing
                                        the start and end indices of the substring.

        Returns:
            List[int]:  A list of integers where each integer represents the total number
                        of substrings that start and end with the same character for the
                        corresponding query range.
        """
        length = len(s)
        res = []
        counts = {}

        # Initialize a dictionary to store prefix counts for each character
        for c in set(s):
            counts[c] = [0] * (length + 1)

        # Fill the prefix counts for each character
        for i in range(1, length + 1):
            for char in counts:
                counts[char][i] = counts[char][i-1] + (1 if s[i-1] == char else 0)

        # Function to get the count of same-end substrings in the range [li, ri]
        def getCount(li, ri):
            """
            Calculate the number of substrings with the same starting and ending character
            within the given range [li, ri].

            Args:
                li (int): The starting index of the range.
                ri (int): The ending index of the range.

            Returns:
                int:    The count of substrings with the same starting and ending character
                        within the specified range.
            """
            count = 0
            for char in counts:
                # Calculate the frequency of the character in the range [li, ri]
                fre = counts[char][ri + 1] - counts[char][li]
                # Add the number of same-end substrings for this character
                count += fre * (fre - 1) // 2
            return count

        # Process each query
        for li, ri in queries:
            # Total same-end substrings = length of substring + count of same-end substrings
            res.append(ri - li + 1 + getCount(li, ri))

        return res

solution = Solution()
s = "abcaab"
print(solution.sameEndSubstringCount(s, [[0,0],[1,4],[2,5],[0,5]]))  # [1,5,5,10]
s = "abcd"
print(solution.sameEndSubstringCount(s, [[0,3]]))  # [4]
s = "hhumfxobnydxhejgcagyuidgjfqutazeuovnavqnybdcastnzjxjvfuszwzntfaiqfryvzvluwgnhybkwoewccjwxgnvbhyyzbkpsqbmdxvapwwusvnxmiffctsdwrucrgqcsbhpnvvlrmnragyknphbptyryfvtaeleygorgobuxuaghyhwilokvhotexdhwvqqeodvydwscjwflclraqrcseicclbrogfuspgsjzkkqypseihojdwhirgyuopgtgazoprqdnjvaesqibqhhsbwzcyhypkkmmrlyrnmpazrthcahjlsygqcmgygndeurczzrajasewjvkspfgwyvmxyvfxrsivbxcwcxgdayftdwzqxdhidoqpigpawpjenxytyfwjjlrgkyedriojvsejwmvwdzvftzededeavoobdgdnetysayqczztxiacwkdgwdklwkinxqlgxxrkiwfopeigmenjecoxqvtzxaaasmbjmlcrjgczumgkbaazhxyfbsrykrrtblltwmuecfflexmijxlmmbdylpbsdmuqvuveiekbgrzhyizedvsfjtsimgamqxyczvmeptfnpopxzdmtwwoeivcntwqjkqmlcxyzoxmqxeuxtkntumyemnrhnwxejyvfaapirrrydlisxtzacyghtpidbgqwrdtxfhupkypxkcbagzxjjxgmzmmkndqawesiawuoprohsawxhnkmrakieoqiielukdnrnlfwstsnyosvdmttkpvfedqtmextohvdcopzwdlxhwydqojxuivplmykmhxvwraoqyluxvgzlhlgqcgmcjjwrqpkxxqccdthmhwthjtdnufercmdnfkfwpdqjcakzflyrqpdnpdnxagynyjtfqbvtwkjpwljbgxmoeuzpixwuvvfxxpktxbdhvynsiwqxzxksfucuvmovkblybbagskbhmxvrzesfnllrluclwmkufhcnxgqmntjoldpjikjkooawxtcilzftjqsdgrwrxucobkubrurvtdri"
print(solution.sameEndSubstringCount(s, [[563,629],[2,558],[52,690],[311,738],[539,1019],[400,993],[584,693],[432,565],[703,788],[368,811],[714,848],[124,774],[631,822],[309,629],[572,766],[67,491],[470,740],[68,599],[382,821],[214,322],[490,1003],[884,1023],[243,274],[95,736],[271,518],[392,413],[735,938],[378,498],[395,637],[17,153],[704,1005],[489,762],[186,810],[207,709],[146,610],[85,403],[770,808],[387,437],[236,654],[17,217],[214,938],[144,875],[703,1022],[265,599],[641,948],[90,715],[140,396],[473,817],[162,745],[543,856],[63,866],[162,892],[407,610],[336,853],[96,998],[359,885],[251,387],[500,994],[81,713],[547,615],[328,748],[358,453],[140,878],[202,457],[843,967],[567,1010],[576,969],[266,636],[1,468],[51,406],[331,472],[25,420],[416,593],[494,1030],[279,986],[110,245],[823,1004],[189,935],[30,461],[224,751],[399,444],[570,760],[531,1001],[205,457],[393,728],[660,754],[205,543],[484,681],[108,566],[76,478],[615,965],[435,938],[465,549],[200,571],[587,1033],[156,490],[243,771],[814,912],[412,486],[626,790]]))

# Time Complexity:
# - Initializing the counts dictionary: O(n)
# - Filling the prefix counts for each character: O(n^2)
# - Processing each query: O(q * |C|), where q is the number of queries and |C| is the number of unique characters in s
# Overall time complexity: O(n^2 + q * |C|)

# Space Complexity:
# - counts dictionary: O(n * |C|), where |C| is the number of unique characters in s
# Overall space complexity: O(n * |C|)
