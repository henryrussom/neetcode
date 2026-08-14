class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_return = 0
        min_value = prices[0]
        for price in prices:
            if price < min_value:
                min_value = price
            if price - min_value >= max_return:
                max_return = price - min_value
        
        return max_return