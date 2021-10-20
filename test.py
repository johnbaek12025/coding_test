import collections
from typing import List


def maxProfit(prices: List[int]) -> int:
    x = prices[0]
    sum = 0
    for i in range(1, len(prices)):                
        if prices[i] <= x:
            x = prices[i]
        elif prices[i] > x:            
            sum += prices[i] - x
            x = prices[i]
    return sum

print(maxProfit(prices = [7,1,5,3,6,4]))