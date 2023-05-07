def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # dp[i][j] = i番目までのAND/OR演算でj個のTrueが出現する組み合わせの数
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        if S[i] == "AND":
            # i番目がANDの場合は、Trueが出現しない場合の数を引く
            for j in range(N + 1):
                dp[i + 1][j] = dp[i][j] * 2 ** (N - j) - dp[i][j]
        else:
            # i番目がORの場合は、Trueが出現する場合の数を足す
            for j in range(N + 1):
                dp[i + 1][j] = dp[i][j] * 2 ** (N - j) + dp[i][j]
    print(dp[N][N])
