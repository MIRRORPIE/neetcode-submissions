class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1:
        # d = {}
        # for s in strs:
        #     s_sort = ''.join(sorted(s))
        #     if s_sort in d:
        #         d[s_sort].append(s)
        #     else:
        #         d[s_sort] = [s]
        # return list(d.values())
            
        # Solution 2:
        anagram_d = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in anagram_d:
                anagram_d[key] = []
            anagram_d[key].append(s)
        return list(anagram_d.values())
                
            
