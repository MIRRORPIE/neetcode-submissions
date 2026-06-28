class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seq = {}
        numset = set(nums)
        for num in numset:
            x,y = 0,0
            if num-1 in numset:
                x = 1
            if num+1 in numset:
                y = 1
            seq[num] = (x,y)

        if seq and all(value == (0,0) for value in seq.values()):
            return 1
        
        
        starts = []
        for key, val in seq.items():
            if val == (0,1):
                starts.append(key)
        
        maxsumseq = [0]
        for num in starts:
            maxsum = 1
            while num+1 in numset:
                num += 1
                maxsum += 1
            maxsumseq.append(maxsum)
        return max(maxsumseq)

