def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    # DPテーブル
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    # DPループ
    for i in range(N + 1):
        for j in range(N + 1):
            if i + j > N:
                break
            # 表が出た時
            if i + 1 <= N:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + X[i])
            # 裏が出た時
            if j + 1 <= N:
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])
                for k in range(M):
                    if i + j + 1 == C[k]:
                        dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + Y[k])
    # 最大値を出力
    print(dp[N][N])
