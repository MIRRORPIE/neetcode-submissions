class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = {}
        # limit = len(nums) // 2

        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        #     if count[num] > limit:
        #         return num


        # Moore's voting algorithm
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            if candidate == n:
                count += 1
            else:
                count -= 1
        return candidate

       
                