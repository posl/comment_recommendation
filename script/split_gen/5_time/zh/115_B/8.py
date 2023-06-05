def main():
    n = int(input())
    prices = [int(input()) for i in range(n)]
    prices.sort(reverse=True)
    prices[0] = prices[0] // 2
    print(sum(prices))
