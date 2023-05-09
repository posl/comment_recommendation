def main():
    N = int(input())
    prices = [int(input()) for i in range(N)]
    prices.sort()
    prices[-1] = int(prices[-1] / 2)
    print(sum(prices))

if __name__ == '__main__':
    main()