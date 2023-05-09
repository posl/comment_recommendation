def solve():
    N, M = map(int, input().split())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        if A <= M:
            jobs.append((A, B))
    jobs.sort()
    dp = [0] * (M + 1)
    for a, b in jobs:
        for i in range(M, a - 1, -1):
            dp[i] = max(dp[i], dp[i - a] + b)
    print(max(dp))

if __name__ == '__main__':
    solve()