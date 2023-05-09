def main():
    P = int(input())
    coins = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
    ans = 0
    for i in coins:
        if P >= i:
            ans += P // i
            P = P % i
    print(ans)

if __name__ == '__main__':
    main()