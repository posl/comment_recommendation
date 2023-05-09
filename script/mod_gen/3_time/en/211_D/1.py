def main():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    MOD = 10**9 + 7
    dp = [0] * N
    dp[0] = 1
    for i in range(N):
        for j in edges[i]:
            dp[j] += dp[i]
            dp[j] %= MOD
    print(dp[-1])

if __name__ == '__main__':
    main()