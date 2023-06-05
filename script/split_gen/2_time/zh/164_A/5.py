def solve():
    N, K = map(int, input().split())
    MOD = 1000000007
    if K == N + 1:
        print(1)
        return
    if K == 1:
        print(N + 1)
        return
    ans = 0
    for i in range(K, N + 2):
        ans += i * (N - i + 2) + 1
        ans %= MOD
    print(ans)
