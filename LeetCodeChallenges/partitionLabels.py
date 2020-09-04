# A string S of lowercase English letters is given.
# We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

# Note:
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.

from typing import Dict, List


class Solution:

    def getLastPositionsByCharacter(self, S: str) -> Dict[chr, int]:
        lastPositions = {}
        for i in range(len(S)-1, -1, -1):
            if S[i] not in lastPositions:
                lastPositions[S[i]] = i
        return lastPositions

    def getNextPartitionStartIndex(self, S: str, startIndex: int, lastPositions: Dict[chr, int]) -> int:
        toHandleSet = set(S[startIndex])
        handledSet = set()
        previousCharacterLastPosition = startIndex
        while (len(toHandleSet) > 0):
            currentCharacter = toHandleSet.pop()
            handledSet.add(currentCharacter)
            # we add all characters that appear between previous and current last position, in our "to handle" set
            if lastPositions[currentCharacter] > previousCharacterLastPosition:
                newItemsList = [
                    c for c in S[previousCharacterLastPosition:lastPositions[currentCharacter]]]
                newSet = set(newItemsList).difference(handledSet)
                toHandleSet.update(newSet)
                previousCharacterLastPosition = lastPositions[currentCharacter]
        return previousCharacterLastPosition+1

    def partitionLabels(self, S: str) -> List[int]:
        result = []
        lastPositions = self.getLastPositionsByCharacter(S)
        startIndex = 0
        while startIndex < len(S):
            nextStartIndex = self.getNextPartitionStartIndex(
                S, startIndex, lastPositions)
            result.append(nextStartIndex-startIndex)
            startIndex = nextStartIndex
        return result


s = Solution()
print(s.partitionLabels('aaabacd'))
