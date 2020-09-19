from typing import List


class Solution:

    def handleInterval(self, interval: List[int], newInterval: List[int], openedInterval: List[int], isNewIntervalHandled: bool, isLast: bool) -> (List[List[int]], List[int], bool):
        if isNewIntervalHandled:
            return interval, openedInterval, True
        elif interval[1] < newInterval[0]:
            if not isLast:
                return [interval], openedInterval, False
            else:
                return[interval, newInterval], openedInterval, True
        elif interval[0] <= newInterval[0] and interval[1] >= newInterval[1]:
            return [interval], openedInterval, True
        elif interval[0] <= newInterval[0] <= interval[1] <= newInterval[1]:
            if openedInterval:
                openedInterval = [openedInterval[0], newInterval[1]]
            else:
                openedInterval = [interval[0], newInterval[1]]
            if isLast:
                return [openedInterval], [], True
        elif newInterval[0] <= interval[0] <= newInterval[1] <= interval[1]:
            if openedInterval:
                openedInterval = [openedInterval[0], interval[1]]
            else:
                openedInterval = [newInterval[0], interval[1]]
            if isLast:
                return [openedInterval], [], True
        elif newInterval[0] <= interval[0] <= interval[1] <= newInterval[1] and not openedInterval:
            return [newInterval], [], True       
        elif interval[0] > newInterval[1]:
            if not openedInterval:
                return [newInterval, interval], [], True
            else:
                return [openedInterval, interval], [], True
        elif openedInterval and openedInterval[1] < interval[1]:
            openedInterval[1] = interval[1]
        return [], openedInterval, False


    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        openedInterval = []
        isNewIntervalHandled = False
        if not intervals:
            return [newInterval]
        for i in range(len(intervals)):
            currentIntervals, openedInterval, isNewIntervalHandled  = self.handleInterval(intervals[i], newInterval, openedInterval, isNewIntervalHandled, i == len(intervals)-1)
            if currentIntervals:
                result += currentIntervals
        return result


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
s = Solution()
print(s.insert(intervals, newInterval))

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
s = Solution()
print(s.insert(intervals, newInterval))

intervals = [[1, 5]]
newInterval = [2, 7]
s = Solution()
print(s.insert(intervals, newInterval))

intervals = [[1, 5]]
newInterval = [0, 6]
s = Solution()
print(s.insert(intervals, newInterval))


intervals = [[1,3],[6,9]]
newInterval = [2, 5]
s = Solution()
print(s.insert(intervals, newInterval))