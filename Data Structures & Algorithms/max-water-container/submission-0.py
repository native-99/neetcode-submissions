class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                width = j-i
                height = min(heights[i],heights[j])
                area = width * height
                result = max(area , result)

        return result