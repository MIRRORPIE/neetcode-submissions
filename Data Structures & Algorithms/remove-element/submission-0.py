class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        count = 0
        j = 0
        while(i < len(nums)):
            #print(nums, "    i:", i, "   j:",j, "    count:",count)
            if nums[i] == val:
                count += 1
                if(j+count < len(nums)):
                    nums[j] = nums[j+count]
                    if(nums[j+count] != val):
                        j += 1
            elif(j+count < len(nums)):
                nums[j] = nums[j+count]
                if(nums[j+count] != val):
                    j += 1
            i += 1

        for i in range(len(nums)-count, len(nums)):
            nums[i] = '_'

        return len(nums)-count