# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a maximal substring consisting of non-space characters only.

# Example:
# Input: "Hello World"
# Output: 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if len(words) == 0:
            return 0
        for i in range(len(words)-1, -1, -1):
            if len(words[i]) > 0:
                return len(words[i])
        return 0


s = Solution()
print(s.lengthOfLastWord("Hello World"))
