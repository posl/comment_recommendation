def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    # dp[i][j]: i回目の手でjを出した時の最大得点
    dp = [[0 for _ in range(3)] for _ in range(n+1)]
    # 1回目の手は何でも良い
    for i in range(3):
        dp[1][i] = [r, s, p][i]
    for i in range(2, n+1):
        # i回目の手でjを出すときの最大得点
        for j in range(3):
            # i回目の手でjを出すときの得点
            point = [r, s, p][j]
            # i回目の手でjを出すときの得点を加える
            dp[i][j] = dp[i-1][j] + point
            # i回目の手でjを出すとき、i-k回目の手でjを出していたら、i回目の手でjを出せないので、i-k回目の手でjを出さない
            if t[i-1] == t[i-k-1]:
                # i-k回目の手でjを出していたときの最大得点
                max_point = max(dp[i-k-1])
                # i-k回目の手でjを出していたときの最大得点を引く
                dp[i][j] -= max_point
    print(max(dp[n]))
