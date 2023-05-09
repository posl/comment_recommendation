def main():
    # 入力
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    # 配列の初期化
    dp = [0] * (N + 1)
    # dp[0]の初期化
    dp[0] = 1
    # dp[i]の計算
    for i in range(1, N + 1):
        # 壊れている床の場合は0通り
        if i in A:
            dp[i] = 0
        # そうでない場合は、1段上がる場合と2段上がる場合の和
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    # 出力
    print(dp[N] % 1000000007)

if __name__ == '__main__':
    main()