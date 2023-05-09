def main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, 18):
        ans += N // 10 ** i * (10 ** i - 10 ** (i - 1))
        ans %= MOD
        ans += max(N % 10 ** i - 10 ** (i - 1) + 1, 0)
        ans %= MOD
    print(ans)
