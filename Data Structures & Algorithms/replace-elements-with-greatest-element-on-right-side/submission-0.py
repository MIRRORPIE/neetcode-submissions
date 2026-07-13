class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ma = max(arr)
        for i, n in enumerate(arr):
            if(n < ma):
                arr[i] = ma
            elif(n == ma and i != len(arr)-1):
                ma = max(arr[i+1:])
                arr[i] = ma
            else:
                arr[i] = -1

        return arr