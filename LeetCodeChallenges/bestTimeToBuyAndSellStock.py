# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        currentMin = prices[0]
        maxDiff = 0

        for _, price in enumerate(prices[1::]):
            if price - currentMin >= maxDiff:
                maxDiff = price - currentMin
            elif price < currentMin:
                currentMin = price

        return maxDiff


s = Solution()
print(s.maxProfit([2, 1, 2, 1, 0, 1, 2]))
