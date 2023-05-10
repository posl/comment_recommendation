def solve(n,k,prices):
    prices.sort()
    return sum(prices[:k])

if __name__ == '__main__':
    solve()