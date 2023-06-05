def solve():
    n = int(input())
    a = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    s = 0
    for i in range(1, n):
        s = (s + a[i]) % MOD
    for i in range(n - 1):
        ans = (ans + a[i] * s) % MOD
        s = (s - a[i + 1]) % MOD
    print(ans)
solve()
