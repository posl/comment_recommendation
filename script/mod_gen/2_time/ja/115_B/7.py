def main():
    N = int(input())
    prices = [int(input()) for _ in range(N)]
    prices.sort()
    print(int((prices[-1] / 2) + sum(prices[:-1])))

if __name__ == '__main__':
    main()