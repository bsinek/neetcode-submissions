class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = -float('inf')
        minBuy = float('inf')
        for price in prices:
            minBuy = min(minBuy, price)
            best = max(best, price - minBuy)
        return best