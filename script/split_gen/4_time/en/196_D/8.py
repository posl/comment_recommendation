def main():
    H, W, A, B = map(int, input().split())
    mod = 10**9+7
    # dp[i][j] = i行目までで、j個のAを使っている通り数
    dp = [[0 for _ in range(A+1)] for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(A+1):
            dp[i+1][j] += dp[i][j]
            if j < A:
                dp[i+1][j+1] += dp[i][j]
    # 横にA個並べる通り数
    def comb(n, r):
        x = 1
        y = 1
        for i in range(r):
            x *= n-i
            y *= i+1
        return x // y
    # 縦にB個並べる通り数
    def comb2(n, r):
        x = 1
        y = 1
        for i in range(r):
            x *= n-i
            y *= i+1
        return x // y
    # 1行目にB個並べる通り数
    def comb3(n, r):
        x = 1
        y = 1
        for i in range(r):
            x *= n-i
            y *= i+1
        return x // y
    ans = 0
    # 1行目にB個並べた通り数を掛ける
    ans = comb3(W, B)
    # 2行目以降について
    for i in range(1, H):
        # 1行目のB個は使い切ったので、A個を使う通り数を掛ける
        ans *= dp[i][A]
        ans %= mod
        # 1行目のB個を使い切っていないので、1行目のB個を使わない通り数を掛ける
        ans *= comb(W-B, B)
        ans %= mod
