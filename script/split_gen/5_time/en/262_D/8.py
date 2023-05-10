def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # sum(A) * (2 ** (N - 1)) % MOD
    ans = 0
    for a in A:
        ans += a
        ans %= MOD
    ans *= pow(2, N - 1, MOD)
    ans %= MOD
    print(ans)
