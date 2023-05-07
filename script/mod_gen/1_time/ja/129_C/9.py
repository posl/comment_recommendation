def main():
    # データの入力
    N,M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    # DPテーブルの初期化
    dp = [0] * (N+2)
    dp[0] = 1
    # 壊れている床を1、壊れていない床を0とする
    broken = [0] * (N+2)
    for a in A:
        broken[a] = 1
    # DPループ
    for i in range(N+1):
        if broken[i] == 1:
            continue
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]
        dp[i+1] %= 1000000007
        dp[i+2] %= 1000000007
    # 答えの出力
    print(dp[N])

if __name__ == '__main__':
    main()