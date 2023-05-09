def main():
    N, M = map(int, input().split())
    X = [int(i) for i in input().split()]
    C_Y = [[int(i) for i in input().split()] for i in range(M)]
    #連続ボーナスの最大値を求める
    bonus = [0 for i in range(N+1)]
    for i in range(M):
        bonus[C_Y[i][0]] = max(bonus[C_Y[i][0]], C_Y[i][1])
    #連続ボーナスの累積和
    for i in range(1, N+1):
        bonus[i] += bonus[i-1]
    #dp[i] = i 回目までのコイントスで得られる最大金額
    dp = [0 for i in range(N+1)]
    for i in range(1, N+1):
        dp[i] = max(dp[i-1]+X[i-1], dp[i-1]+bonus[i])
    print(dp[N])
