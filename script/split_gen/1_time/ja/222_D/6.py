def solve():
    # 標準入力から入力値を取得する
    N = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    # 初期処理
    MOD = 998244353
    # 処理
    # dp[i][j] = (i番目までの数列で、j番目の要素までを決めたときの場合の数)
    dp = [[0 for j in range(max(b_list)+1)] for i in range(N)]
    for j in range(a_list[0], b_list[0]+1):
        dp[0][j] = 1
    for i in range(1, N):
        for j in range(a_list[i], b_list[i]+1):
            dp[i][j] = sum(dp[i-1][:j+1]) % MOD
    # 出力
    print(sum(dp[N-1]) % MOD)
