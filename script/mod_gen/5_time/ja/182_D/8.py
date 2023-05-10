def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.append(0)
    # dp[i] = 動作開始時から終了時までのロボットの座標の最大値
    dp = [0] * (N+1)
    dp[0] = 0
    for i in range(N):
        dp[i+1] = dp[i] + A[i]
    #print(dp)
    # dp2[i] = 動作開始時から終了時までのロボットの座標の最大値
    dp2 = [0] * (N+1)
    dp2[0] = 0
    for i in range(N):
        dp2[i+1] = dp2[i] + dp[i+1]
    #print(dp2)
    # dp3[i] = 動作開始時から終了時までのロボットの座標の最大値
    dp3 = [0] * (N+1)
    dp3[0] = 0
    for i in range(N):
        dp3[i+1] = dp3[i] + dp2[i+1]
    #print(dp3)
    print(max(dp3))

if __name__ == '__main__':
    solve()