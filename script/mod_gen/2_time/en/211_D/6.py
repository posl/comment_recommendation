def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[1])
    print(edges)
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N):
        for a, b in edges:
            if i == a:
                dp[b] += dp[a]
            if i == b:
                dp[a] += dp[b]
    print(dp[N] % (10 ** 9 + 7))

if __name__ == '__main__':
    main()