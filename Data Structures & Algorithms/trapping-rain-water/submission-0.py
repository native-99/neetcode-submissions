class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        for i in range(len(height)):
            left_max = 0
            right_max = 0

            for l in range(i+1):
                left_max = max(left_max,height[l])

            for r in range(i,len(height)):
                right_max = max(right_max,height[r])

            water = min(left_max,right_max)-height[i]

            result+=water

        return result