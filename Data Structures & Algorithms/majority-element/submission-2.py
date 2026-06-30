class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = {}
        limit = len(nums)//2
        for num in nums:
            if num in s:
                s[num] += 1
                if(s[num] > limit):
                    return num
            else:
                s[num] = 1
                if(s[num] > limit):
                    return num
        