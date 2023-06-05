def main():
    n = int(input())
    mod = 998244353
    ans = 0
    for i in range(1, 19):
        if n < 10 ** i:
            ans += i * (n - 10 ** (i - 1) + 1)
            break
        else:
            ans += i * (10 ** i - 10 ** (i - 1))
    print(ans % mod)

if __name__ == '__main__':
    main()