def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    # dp[i][j] : i回目までの戦いでjを出した場合の最大得点
    dp = [[0 for j in range(3)] for i in range(N)]
    # 初期化
    for i in range(N):
        if T[i] == 'r':
            dp[i][0] = P
        elif T[i] == 's':
            dp[i][1] = R
        else:
            dp[i][2] = S
    # dp
    for i in range(K, N):
        for j in range(3):
            dp[i][j] = max(dp[i - K][(j + 1) % 3], dp[i - K][(j + 2) % 3]) + dp[i][j]
    # print(dp)
    print(max(dp[N - 1]))
