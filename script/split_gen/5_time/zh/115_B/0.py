def main():
    N = int(input())
    prices = []
    for i in range(N):
        prices.append(int(input()))
    max_price = max(prices)
    total = sum(prices)
    total -= max_price / 2
    print(int(total))
