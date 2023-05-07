def main():
    N = int(input())
    prices = []
    for _ in range(N):
        prices.append(int(input()))
    prices.sort(reverse=True)
    ans = prices[0] / 2 + sum(prices[1:])
    print(ans)

if __name__ == '__main__':
    main()