def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(N):
        ans += pow(2, i, MOD) * pow(2, N - i - 1, MOD) * A[i]
        ans %= MOD
    print(ans)
