def main():
    n = int(input())
    prices = []
    for i in range(n):
        prices.append(int(input()))
    prices.sort()
    prices[-1] = prices[-1] / 2
    print(int(sum(prices)))
