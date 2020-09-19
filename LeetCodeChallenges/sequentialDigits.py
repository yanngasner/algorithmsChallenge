from typing import List

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