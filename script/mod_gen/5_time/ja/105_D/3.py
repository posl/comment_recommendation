def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    MOD = M
    from collections import defaultdict
    d = defaultdict(int)
    for s in S:
        d[s % MOD] += 1
    ans = 0
    for k, v in d.items():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()