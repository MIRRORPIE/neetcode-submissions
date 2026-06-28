class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        maxmatch = ''
        for i in range(len(strs)):
            if i == 0:
                length = min(len(strs[i]), len(strs[i+1]))
                for j in range(length):
                    if strs[i][j] != strs[i+1][j]:
                        maxmatch = strs[i+1][:j]
                        break
                else:
                    maxmatch = strs[i+1][:length]
            else:
                length = min(len(maxmatch), len(strs[i]))
                for j in range(length):
                    if maxmatch[j] != strs[i][j]:
                        maxmatch = strs[i][:j]
                        break
                else:
                    maxmatch = strs[i][:length]
        return maxmatch