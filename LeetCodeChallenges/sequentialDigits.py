# from typing import List
# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
# Return a sorted list of all the integers in the range[low, high] inclusive that have sequential digits.


# Example 1:
# Input: low = 100, high = 300
# Output: [123, 234]

# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234, 2345, 3456, 4567, 5678, 6789, 12345]


# Constraints:
# 10 <= low <= high <= 10 ^ 9


class Solution:
    def getAllValidDigits(self, n: int):
        result = []
        for i in range(1, 9-n+2):
            result.append(int(''.join([str(i+k) for k in range(n)])))
        return result

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        potentialValidDigits = []
        for i in range(len(str(low)), len(str(high))+1):
            potentialValidDigits += self.getAllValidDigits(i)
        validDigits = []
        for digit in potentialValidDigits:
            if (low <= digit <= high):
                validDigits.append(digit)
        return validDigits


s = Solution()
print(s.sequentialDigits(100, 1000))
