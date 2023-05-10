def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        for j in a:
            if i - j >= 0 and dp[i - j] >= 0:
                dp[i] = max(dp[i], dp[i - j] * 10 + j)
    print(dp[n])
