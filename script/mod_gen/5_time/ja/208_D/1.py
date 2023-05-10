def main():
    N, M = map(int, input().split())
    INF = 10**9
    # dp[i][j]は都市iから都市jへの最短距離
    dp = [[INF for i in range(N+1)] for j in range(N+1)]
    # 道路の情報をdpに格納
    for i in range(M):
        A, B, C = map(int, input().split())
        dp[A][B] = C
    # dpの初期化
    for i in range(N+1):
        dp[i][i] = 0
    # dpの更新
    # dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    # 答えの計算
    ans = 0
    for s in range(1, N+1):
        for t in range(1, N+1):
            for k in range(1, N+1):
                if s == t or s == k or t == k:
                    continue
                ans += dp[s][t]
    print(ans)

if __name__ == '__main__':
    main()