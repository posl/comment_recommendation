def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = defaultdict(int)
    for _ in range(M):
        c, y = map(int, input().split())
        C[c] = y
    dp = [0 for _ in range(N+1)]
    for i in range(N):
        dp[i+1] = max(dp[i+1], dp[i]+X[i])
        for j in range(i+1, N):
            if C[j-i] > 0:
                dp[j+1] = max(dp[j+1], dp[i]+X[i]+C[j-i]*(j-i))
    print(dp[N])

if __name__ == '__main__':
    main()