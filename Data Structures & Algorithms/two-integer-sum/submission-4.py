class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        i = 0
        while(i < len(nums)):
            numset = set(nums[i+1::])
            if(target - nums[i] in numset):
                x = i
                break
            else:
                i += 1
        ynum = target - nums[x]
        for j, num in enumerate(nums):
            if(num == ynum and x != j):
                return [x, j]





            

        




            
        
            


