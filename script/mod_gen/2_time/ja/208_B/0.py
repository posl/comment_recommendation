def main():
    P = int(input())
    coins = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
    ans = 0
    for i in range(31, -1, -1):
        ans += P // coins[i]
        P = P % coins[i]
    print(ans)

if __name__ == '__main__':
    main()