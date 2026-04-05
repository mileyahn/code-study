class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val, max_val = 10**4, 0
        out = 0
        for i, price in enumerate(prices):
            if min_val > price:
                min_val = price
            elif max_val <= price:
                max_val = price
                out = max_val - min_val
            elif out < price - min_val:
                max_val = price
                out = price - min_val
        return out