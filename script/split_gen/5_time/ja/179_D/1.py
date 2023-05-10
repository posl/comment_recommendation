def main():
    # 標準入力を取得
    n, k = map(int, input().split())
    L = []
    R = []
    for i in range(k):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    # 計算
    # dp[i] = マスiに到達するルートの数
    # dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-K]
    dp = [0] * (n+1)
    dp[1] = 1
    s = 0
    for i in range(2, n+1):
        for j in range(k):
            if i - L[j] >= 0:
                s += dp[i-L[j]]
            if i - R[j]-1 >= 0:
                s -= dp[i-R[j]-1]
        dp[i] = s % 998244353
    print(dp[n])
