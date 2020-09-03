class Solution:   
    def repeatedSubstringPattern(self, s: str) -> bool:
        length=len(s)
        for i in range(1,min(int(length/2), 10000)+1):
            if length % i != 0:
                continue    
            base = s[0:i]        
            for j in range(1, int(length/i)):
                if s[j*i:(j+1)*i] != base:
                    break
                elif j==int(length/i)-1:
                    return True
        return False

s=Solution()
print(s.repeatedSubstringPattern("testtest"))

