def main():
    p = int(input())
    coins = [10**i for i in range(1, 8)]
    coins.reverse()
    ans = 0
    for c in coins:
        ans += p // c
        p %= c
    print(ans)

if __name__ == '__main__':
    main()