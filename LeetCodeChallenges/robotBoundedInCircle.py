# The robot performs the instructions given in order, and repeats them forever.
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.


# Example 1:
# Input: "GGLLGG"
# Output: true
# Explanation:
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

# Example 2:
# Input: "GG"
# Output: false
# Explanation:
# The robot moves north indefinitely.

# Example 3:
# Input: "GL"
# Output: true
# Explanation:
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


class Solution:

    def updatePosition(self, instruction: chr, x: int, y: int, direction: int) -> (int, int, int):
        if (instruction == 'G'):
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
        elif (instruction == 'R'):
            direction = (direction+1) % 4
        elif (instruction == 'L'):
            direction = (direction+3) % 4
        return x, y, direction

    def isRobotBounded(self, instructions: str) -> bool:
        direction = initialDirection = 0
        x = initialX = 0
        y = initialY = 0
        for instruction in instructions:
            x, y, direction = self.updatePosition(instruction, x, y, direction)
        return (x == initialX and y == initialY or direction != initialDirection)


s = Solution()
print(s.isRobotBounded("GGLLGG"))
