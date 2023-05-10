def main():
    n = int(input())
    prices = []
    for i in range(n):
        prices.append(int(input()))
    prices.sort(reverse=True)
    prices[0] = int(prices[0] / 2)
    print(sum(prices))

if __name__ == '__main__':
    main()