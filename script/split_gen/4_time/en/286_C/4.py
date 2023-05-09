def main():
    # input
    n, a, b = map(int, input().split())
    s = input()
    # compute
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = dp[i] + a
        for j in range(i):
            if s[i] == s[j]:
                dp[i + 1] = min(dp[i + 1], dp[j] + b)
    ans = dp[n]
    # output
    print(ans)
