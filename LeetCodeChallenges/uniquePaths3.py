# On a 2-dimensional grid, there are 4 types of squares:
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.


# Example 1:
# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

# Example 2:
# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

# Example 3:
# Input: [[0,1],[2,0]]
# Output: 0
# Explanation:
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.


# Note:
# 1 <= grid.length * grid[0].length <= 20


from typing import List
import copy


class ElementInPath:
    def __init__(self, position: (int, int), remaining: int, grid: List[List[int]]):
        self.position = position
        self.remaining = remaining
        self.grid = grid


class Solution:

    def getInfos(self, grid: List[List[int]]) -> (int, (int, int), (int, int)):
        length = 0
        begin = (0, 0)
        end = (0, 0)
        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                if element >= 0:
                    length += 1
                if element == 1:
                    begin = (i, j)
                if element == 2:
                    end = (i, j)
        return length, begin, end

    def getAcceptedNext(self, element: ElementInPath) -> List[ElementInPath]:
        if not 0 <= element.position[0] < len(element.grid) or not 0 <= element.position[1] < len(element.grid[0]):
            return []
        elif element.grid[element.position[0]][element.position[1]] == 2 and element.remaining == 0:
            return [element]
        elif element.grid[element.position[0]][element.position[1]] == 0 and element.remaining > 0:
            newGrid = copy.deepcopy(element.grid)
            newGrid[element.position[0]][element.position[1]] = -1
            return self.getAcceptedPathesFrom(ElementInPath(element.position, element.remaining, newGrid))
        else:
            return []

    def getAcceptedPathesFrom(self, element: ElementInPath) -> List[ElementInPath]:
        acceptedPathes = []
        next = (element.position[0]-1, element.position[1])
        acceptedPathes += self.getAcceptedNext(ElementInPath(next, element.remaining-1, element.grid))
        next = (element.position[0]+1, element.position[1])
        acceptedPathes += self.getAcceptedNext(ElementInPath(next, element.remaining-1, element.grid))
        next = (element.position[0], element.position[1]-1)
        acceptedPathes += self.getAcceptedNext(ElementInPath(next, element.remaining-1, element.grid))
        next = (element.position[0], element.position[1]+1)
        acceptedPathes += self.getAcceptedNext(ElementInPath(next, element.remaining-1, element.grid))
        return acceptedPathes

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        pathLength, begin, end = self.getInfos(grid)
        pathes = self.getAcceptedPathesFrom(ElementInPath(begin, pathLength-1, grid))
        return len(pathes)


s = Solution()

Input = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
print(s.uniquePathsIII(Input))

Input = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
print(s.uniquePathsIII(Input))
