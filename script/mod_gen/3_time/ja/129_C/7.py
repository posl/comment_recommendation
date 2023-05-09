def main():
    # 入力
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    # 答えを格納する変数
    ans = 0
    # 処理
    # 0段目から順に移動可能な場合の数を格納する配列
    dp = [0] * N
    # 0段目から移動可能な場合の数は1通り
    dp[0] = 1
    # 1段目から順に移動可能な場合の数を計算
    for i in range(1, N):
        # 1段目の場合
        if i == 1:
            # 壊れている床がある場合
            if i in A:
                dp[i] = 0
            # 壊れている床がない場合
            else:
                dp[i] = dp[i-1]
        # 2段目以降の場合
        else:
            # 壊れている床がある場合
            if i in A:
                dp[i] = 0
            # 壊れている床がない場合
            else:
                # 1段前と2段前の移動可能な場合の数の和
                dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    # 答え
    ans = dp[N-1]
    # 出力
    print(ans)

if __name__ == '__main__':
    main()