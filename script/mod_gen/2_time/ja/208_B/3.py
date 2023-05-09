def main():
    P = int(input())
    coin = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    coin.reverse()
    ans = 0
    for i in range(10):
        ans += P // coin[i]
        P %= coin[i]
    print(ans)

if __name__ == '__main__':
    main()