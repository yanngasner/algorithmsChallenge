# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows").
# Your friend will use successive guesses and hints to eventually derive the secret number.
# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.
# Please note that both secret number and friend's guess may contain duplicate digits.
# Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

# Example 1:
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

# Example 2:
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

from typing import List
from itertools import groupby


class Solution:

    def getBullsAndReturnRemainings(self, secretList: List[chr], guessList: List[chr]) -> (int, List[chr], List[chr]):
        assert len(secretList) == len(guessList)
        remainingSecretList = []
        remainingGuessList = []
        bulls = 0
        for i in range(len(secretList)):
            if secretList[i] == guessList[i]:
                bulls += 1
            else:
                remainingSecretList.append(secretList[i])
                remainingGuessList.append(guessList[i])
        return bulls, remainingSecretList, remainingGuessList

    def getCows(self, secretList: List[chr], guessList: List[chr]) -> int:
        assert len(secretList) == len(guessList)
        cows = 0
        secretChars = dict((item, len(list(group))) for item, group in groupby(sorted(secretList)))
        for guess in guessList:
            if (guess in secretChars):
                cows += 1
                secretChars[guess] -= 1
                if secretChars[guess] == 0:
                    secretChars.pop(guess)
        return cows

        # for i in range(len(secretList)):
        #     if secretList[i] in remainingGuessList:
        #         cows += 1
        #         remainingGuessList.remove(secretList[i])
        return cows

    def getHint(self, secret: str, guess: str) -> str:
        secretList = list(secret)
        guessList = list(guess)
        bulls, secretList, guessList = self.getBullsAndReturnRemainings(secretList, guessList)
        cows = self.getCows(secretList, guessList)
        return f"{bulls}A{cows}B"


s = Solution()
s.getHint("8226526357", "7965193296")

"8226526357"
"7965193296"
