class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = {}
        for num in nums:
            if num in s:
                s[num] += 1
            else:
                s[num] = 1
        for key, val in s.items():
            if val > len(nums) // 2:
                return key