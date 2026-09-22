class Solution:
    # brute force 
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for day, price1 in enumerate(prices):
            for tomorrow, price2 in enumerate(prices[day + 1:]):
                profit = price2 - price1
                maxP = max(maxP, profit)
        return maxP