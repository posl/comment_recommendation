def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    for i in range(60):
        c = 0
        for a in A:
            if a & (1 << i):
                c += 1
        ans += (c * (N - c) * (1 << i)) % MOD
        ans %= MOD
    print(ans)
