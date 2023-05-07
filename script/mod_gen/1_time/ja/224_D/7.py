def main():
    M = int(input())
    E = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))
    INF = 10**10
    dp = [[INF] * 9 for _ in range(1 << 8)]
    dp[0][0] = 0
    for s in range(1 << 8):
        for v in range(9):
            for i in range(8):
                if (s >> i) & 1:
                    continue
                for u, w in E:
                    if (P[i] == u and v == w) or (P[i] == w and v == u):
                        dp[s | (1 << i)][P[i] - 1] = min(dp[s | (1 << i)][P[i] - 1], dp[s][v] + 1)
    if dp[-1][-1] == INF:
        print(-1)
    else:
        print(dp[-1][-1])

if __name__ == '__main__':
    main()