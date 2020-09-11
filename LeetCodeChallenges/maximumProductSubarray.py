from typing import List
from functools import reduce

class Solution:
    def getWithoutZeroListsAndHasZero(self, nums: List[int]) -> List[List[int]]:
        result = []
        hasZero = False
        currentList = []
        for i in nums:
            if i == 0:
                hasZero = True
                if currentList:
                   result.append(currentList)
                   currentList=[]
            else:
                currentList.append(i)
        if currentList:
                   result.append(currentList)
        return result, hasZero

    def getResultAfterFirstNegative(self, nums:List[int]) -> int:
        result = 1
        start = False
        for i in range(0, len(nums)):
            if not start:
                if nums[i] < 0:
                    start = True
                if i == len(nums) - 1:
                    return nums[i]
            else:
                result *= nums[i]
        return result

    def getMaxProduct(self, nums:List[int]) -> int:
        product = reduce(lambda current, next: current*next,nums)
        if product > 0:
            return product
        #compute after first 0, and before last 0:
        return max(self.getResultAfterFirstNegative(nums),self.getResultAfterFirstNegative(nums[::-1]))      

    def maxProduct(self, nums: List[int]) -> int:
        withoutZeroLists, hasZeros = self.getWithoutZeroListsAndHasZero(nums)
        if len(withoutZeroLists) == 0:
            return 0
        if len(withoutZeroLists) == 1 and not hasZero:
            return self.getMaxProduct(withoutZeroLists[0])
        if len(withoutZeroLists) == 1 and hasZero:        
            return max(0, self.getMaxProduct(withoutZeroLists[0]))   
        return max(0, *[self.getMaxProduct(withoutZeroList) for withoutZeroList in withoutZeroLists])

s = Solution()
print(s.maxProduct([0,-1,2,-1,4,0,0,5,1]))