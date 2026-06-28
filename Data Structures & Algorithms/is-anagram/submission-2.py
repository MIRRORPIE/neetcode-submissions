class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = dict()
        t1 = dict()
        for ch in s:
            if ch in s1:
                s1[ch] += 1
            else:
                s1[ch] = 1
        for ch in t:
            if ch in t1:
                t1[ch] += 1
            else:
                t1[ch] = 1
        if s1 == t1:
            return True
        return False

