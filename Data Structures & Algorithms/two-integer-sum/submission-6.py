class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = set()
        j = 0
        while(j < len(nums)):
            if(target - nums[j] in numset):
                y = j
                break
            else:
                numset.add(nums[j])
                j += 1
        target = target - nums[y]
        for i in range(len(nums)):
            if(nums[i] == target):
                x = i
                break
        return [x,y]

        





            

        




            
        
            


