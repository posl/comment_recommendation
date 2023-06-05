def main():
    n, x, y = map(int, input().split())
    #print(n, x, y)
    #print(type(n), type(x), type(y))
    #宝石的最大数量
    MAX = 10
    #dp[i]表示i个宝石的最大数量
    dp = [0] * (MAX + 1)
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + x
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + y)
    print(dp[n])
