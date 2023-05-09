def main():
    P = int(input())
    coin = [1]
    for i in range(2, 11):
        coin.append(coin[-1]*i)
    ans = 0
    for c in reversed(coin):
        ans += P//c
        P %= c
    print(ans)

if __name__ == '__main__':
    main()