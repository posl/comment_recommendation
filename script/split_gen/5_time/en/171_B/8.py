def solve(n,k,prices):
    prices.sort()
    return sum(prices[:k])
