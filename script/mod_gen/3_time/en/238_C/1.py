def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, len(str(N)) + 1):
        ans += (N // (10 ** i) * (10 ** (i - 1))) % MOD
        ans %= MOD
        ans += max(0, (N % (10 ** i)) - (10 ** (i - 1)) + 1) % MOD
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()