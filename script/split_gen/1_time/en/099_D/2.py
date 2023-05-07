def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 3色で塗り分ける場合のコストを計算
    cost = [[0] * 3 for _ in range(C)]
    for i in range(N):
        for j in range(N):
            cost[c[i][j] - 1][(i + j) % 3] += 1
    # 3色で塗り分けたときのコストを計算
    dp = [[float("inf")] * C for _ in range(3)]
    for i in range(C):
        dp[0][i] = D[i][0] * cost[i][0]
    for i in range(1, 3):
        for j in range(C):
            for k in range(C):
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + D[j][i] * cost[j][i])
    print(min(dp[2]))
