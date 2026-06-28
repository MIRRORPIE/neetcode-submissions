class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        starts = []
        numset = set(nums)
        for num in numset:
            if num-1 not in numset and num+1 in numset:
                starts.append(num)
        if len(starts) == 0 and len(nums) > 0:
            return 1

        maxsumseq = [0]
        for num in starts:
            maxsum = 1
            while num+1 in numset:
                num += 1
                maxsum += 1
            maxsumseq.append(maxsum)
        return max(maxsumseq)

