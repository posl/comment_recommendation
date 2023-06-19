def main():
    n = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, 19):
        if n < 10 ** i:
            ans += (n - 10 ** (i - 1) + 1) * i
            break
        else:
            ans += (10 ** i - 10 ** (i - 1)) * i
    ans %= mod
    print(ans)

if __name__ == '__main__':
    main()