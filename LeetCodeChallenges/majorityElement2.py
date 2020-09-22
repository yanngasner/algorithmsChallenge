# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:
# Input: [3,2,3]
# Output: [3]

# Example 2:
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]


from typing import List
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = dict()
        count = 0
        for num in nums:
            counts[num] = counts[num] + 1 if num in counts else 1
            count += 1
        threshold = math.floor(count/3)
        return [key for key, value in counts.items() if value > threshold]


s = Solution()
print(s.majorityElement([3, 2, 3]))
