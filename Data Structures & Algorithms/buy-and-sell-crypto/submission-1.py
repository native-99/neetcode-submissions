class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0
        left = 0
        right = 1

        while right < len(prices):

            if prices[left] < prices[right]:
                profit = prices[right]-prices[left]

                result = max(profit , result)

            else:
                left = right

            right+=1

        return result