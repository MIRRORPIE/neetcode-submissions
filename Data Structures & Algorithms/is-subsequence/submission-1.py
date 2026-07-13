class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        flag = True
        for c1 in s:
            if i == len(t):
                return False
            while i < len(t):
                c2 = t[i]
                if c1 == c2:
                    i += 1
                    break
                else:
                    i += 1
        return True

            