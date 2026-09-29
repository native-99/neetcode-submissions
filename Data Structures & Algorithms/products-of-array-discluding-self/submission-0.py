class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lenght = len(nums)
        result = [1] * lenght

        prefix = 1

        for i in range(lenght):
            result[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1

        for i in range(lenght-1,-1,-1):
            result[i] = result[i] * suffix
            suffix  = suffix * nums[i]

        return result 