class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        n = len(nums)

        while i < n:
            if nums[i]==val:
                for j in range(i,n-1):
                    nums[j]=nums[j+1]
                n-=1
            else:
                i+=1
        return n
 