def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, 19):
        ans += N // (10 ** i) * (10 ** (i - 1)) + min(max(N % (10 ** i) - (10 ** (i - 1)) + 1, 0), 10 ** (i - 1))
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()