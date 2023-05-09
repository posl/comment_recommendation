def main():
    n, w = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        tmp_a, tmp_b = map(int, input().split())
        a.append(tmp_a)
        b.append(tmp_b)
    # dp[i][j] := i 番目までの品物の中から、重さが j 以下となるように選んだときの、価値の総和の最大値
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    # dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i - 1]] + b[i - 1])
    # i 番目の品物を選ぶ場合、選ばない場合のどちらか
    # i 番目の品物を選ばない場合、dp[i - 1][j] と同じ
    # i 番目の品物を選ぶ場合、dp[i - 1][j - a[i - 1]] + b[i - 1]
    # i 番目の品物を選ぶ場合の価値は、i 番目の品物を選ぶ前の価値に i 番目の品物の価値を足す
    # i 番目の品物を選ぶ場合の重さは、i 番目の品物を選ぶ前の重さから i 番目の品物の重さを引く
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j - a[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i - 1]] + b[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n][w])
