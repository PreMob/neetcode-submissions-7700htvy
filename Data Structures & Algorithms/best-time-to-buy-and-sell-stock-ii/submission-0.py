class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        buy = 0
        

        for i in range(len(prices)) :
            if prices[i] > prices[buy]:
                profit = prices[i] - prices[buy]
                total_profit = total_profit + profit
            buy = i

        return total_profit