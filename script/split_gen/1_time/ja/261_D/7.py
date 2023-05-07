def main():
    # 入力
    N,M = map(int,input().split())
    X = [int(x) for x in input().split()]
    C = [0]*M
    Y = [0]*M
    for i in range(M):
        C[i],Y[i] = map(int,input().split())
    # 処理
    # dp[i] = i回目までのコイントスでもらえる最大の金額
    dp = [0]*(N+1)
    # 連続ボーナスを受け取る
    for i in range(M):
        dp[C[i]] = max(dp[C[i]],Y[i])
    # 連続ボーナスを受け取る
    for i in range(N):
        dp[i+1] = max(dp[i+1],dp[i])
    # 連続ボーナスを受け取っていない場合の金額を計算
    for i in range(N):
        if dp[i+1] == dp[i]:
            dp[i+1] = dp[i] + X[i]
    # 出力
    print(max(dp))
