def main():
    n = int(input())
    prices = []
    for i in range(n):
        prices.append(int(input()))
    prices.sort()
    prices.pop()
    prices[0] = prices[0] / 2
    print(int(sum(prices)))
main()
import sys

if __name__ == '__main__':
    main()