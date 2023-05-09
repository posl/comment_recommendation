def solve():
    N = int(input())
    *A, = map(int, input().split())
    MOD = 10**9 + 7
    ans = 0
    for i in range(61):
        cnt = 0
        for a in A:
            if a & (1 << i):
                cnt += 1
        ans += cnt * (N - cnt) * (1 << i)
        ans %= MOD
    print(ans)
